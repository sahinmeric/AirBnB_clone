#!/usr/bin/python3
"""
This script has Base model class
"""
import models
import uuid
from datetime import datetime
format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base model class"""
    def __init__(self, *args, **kwargs):
        """Initialization of base model class"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if hasattr(self, "created_at"):
                self.created_at = datetime.strptime(kwargs["created_at"], format)
            if hasattr(self, "updated_time"):
                self.updated_at = datetime.strptime(kwargs["updated_at"], format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self) -> str:
        """String presentation of BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict_upd = self.__dict__.copy()
        if "created_at" in dict_upd:
            dict_upd["created_at"] = dict_upd["created_at"].strftime(format)
        if "updated_at" in dict_upd:
            dict_upd["updated_at"] = dict_upd["updated_at"].strftime(format)
        dict_upd["__class__"] = self.__class__.__name__
        return dict_upd

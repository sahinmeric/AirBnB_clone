#!/usr/bin/python3
"""
This script has Base model class
"""
import models
import uuid
from datetime import datetime as dt

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
                self.created_at = dt.strptime(kwargs["created_at"], format)
            if hasattr(self, "updated_at"):
                self.updated_at = dt.strptime(kwargs["updated_at"], format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self) -> str:
        """String presentation of BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current dt
        """
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_upd = self.__dict__.copy()
        dict_upd["__class__"] = type(self).__name__
        dict_upd['created_at'] = self.__dict__['created_at'].isoformat()
        dict_upd['updated_at'] = self.__dict__['updated_at'].isoformat()
        return dict_upd

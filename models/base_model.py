#!/usr/bin/python3
"""
This script has Base model class
"""
from pyexpat import model
import models
import uuid
from datetime import datetime
format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base model class"""
    def __init__(self, *args, **kwargs):
        """Initialization"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or "updated_at":
                    setattr(self, k, datetime.strptime(v,format))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at #this should be executed when instance first time created
        models.storage.new(self)

    def __str__(self) -> str:
        """String presentation of BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
       """returns a dictionary containing all keys/values of __dict__ of the instance"""
       return self.__dict__
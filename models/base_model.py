#!/usr/bin/python3
"""
This script has Base model class
"""

import uuid
from datetime import datetime


class BaseModel:
    """Base model class"""
    def __init__(self):
        """Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at #this should be executed when instance first time created
    

    def __str__(self) -> str:
        """String presentation of BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
       """returns a dictionary containing all keys/values of __dict__ of the instance"""
       return self.__dict__
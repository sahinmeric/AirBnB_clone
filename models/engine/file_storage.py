#!/usr/bin/python3
"""
this script contains a class to serialize and deserialize instances
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    this class serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "/.file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__,obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic = {}
        for k in self.__objects.keys():
            dic[k] = self.__objects[k].to_dict()
        
        with open(self.__file_path, 'w') as f:
            json.dump(dic, f)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for k in data:
                    pass #TODO
        except:
            pass
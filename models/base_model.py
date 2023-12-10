#!/usr/bin/python3
"""Base Model Documentation"""

from datetime import datetime as dt
from uuid import uuid4

class BaseModel:
    """BaseModel Class for the project"""
    
    def __init__(self, **kwargs):
        """Initilization of the BaseModel object"""
        self.id = str(uuid4())
        self.created_at = dt.now()
        self.updated_at = self.created_at

    def __str__(self):
        """returns string representation of the BaseModel object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the public instance attribute 'updated_at' with the current datetime"""
        self.updated_at = dt.now()

    def to_dict(self):
        """returns dictionary of keys/values from the BaseModel object"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.__dict__

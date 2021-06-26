#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods"""
import uuid
from datetime import datetime


class BaseModel:
    """ define class base"""

    def __init__(self):
        """ Initialize public instance attributes """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ return string representation of basemodel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ dictionary representation of basemodel"""
        c_dict = dict(self.__dict__)
        c_dict['_class_'] = self.__class__.__name__
        c_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        c_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return c_dict

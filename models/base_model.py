#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods"""
import uuid
from datetime import datetime


class BaseModel:
    """ define class base"""

    def __init__(self, *args, **kwargs):
        """ Initialize public instance attributes """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

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
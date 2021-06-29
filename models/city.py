#!/usr/bin/python3
'''City Class'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    Inherits Public class attributes from BaseModel:

    state_id: <str> will be the State.id
    name:     <str>
    '''
    state_id = ""
    name = ""

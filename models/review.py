#!/usr/bin/python3
'''Review Class'''



from models.base_model import BaseModel

class Review(BaseModel):
    '''
    Inherits Public class attributes from BaseModel:

    place_id: <str> will be the Place.id
    user_id:  <str> will be the User.id
    text:     <str>
    '''
    place_id = ""
    user_id = ""
    text = ""

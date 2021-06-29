#!/usr/bin/python3
''' Place Class '''



from models.base_model import BaseModel

class Place(BaseModel):
    '''
    Inherits Public class attributes from BaseModel:

    city_id:        <str> will be the City.id
    user_id:        <str> will be the User.id
    name:           <str>
    description:    <str>
    number_rooms:   <int> 0
    max_guest:      <int> 0
    price_by_night: <int> 0
    latitude:       <float> 0.0
    longitude:      <float> 0.0
    amenity_ids:    <list> will be the list of Amenity.id
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
#!/usr/bin/python3
"""
A module Place that inherits from BaseModel
"""


import models
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class Place that inherits from BaseModel
    """

    city_id = ""  # the City.id
    user_id = ""  # the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # the list[str] of Amenity.id

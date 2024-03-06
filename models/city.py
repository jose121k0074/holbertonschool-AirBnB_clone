#!/usr/bin/python3
"""
A module City that inherits from BaseModel
"""


import models
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class City that inherits from BaseModel
    """

    state_id = ""  # the State.id
    name = ""

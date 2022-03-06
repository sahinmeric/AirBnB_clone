#!/usr/bin/python3
"""Module for place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place model"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """Init for the user model"""
        super().__init__(*args, **kwargs)

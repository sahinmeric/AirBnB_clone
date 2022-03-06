#!/usr/bin/python3
"""Module for Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity model"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init for the amenity model"""
        super().__init__(*args, **kwargs)

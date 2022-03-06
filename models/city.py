#!/usr/bin/python3
"""Module for City"""
from models.base_model import BaseModel


class City(BaseModel):
    """City model"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init for the city model"""
        super().__init__(*args, **kwargs)

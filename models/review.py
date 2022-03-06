#!/usr/bin/python3
"""Module for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review model"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Init for the review model"""
        super().__init__(*args, **kwargs)

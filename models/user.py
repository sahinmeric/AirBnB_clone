#!/usr/bin/python3
"""Module for Use"""
from models.base_model import BaseModel


class User(BaseModel):
    """User model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Init for the user model"""
        super().__init__(*args, **kwargs)

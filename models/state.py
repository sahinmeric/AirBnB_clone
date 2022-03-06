#!/usr/bin/python3
"""Module for State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State model"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init for the state model"""
        super().__init__(*args, **kwargs)

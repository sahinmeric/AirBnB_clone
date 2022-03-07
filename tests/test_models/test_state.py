#!/usr/bin/python3
"""Unittest for state"""
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """class tests for state"""

    def checkdocst(self):
        """check docstring"""
        self.assertIsNotNone(State.__doc__)

    def createstt(self):
        """tests for state"""
        stt = State()
        self.assertIsInstance(stt, State)
        self.assertIsInstance(stt, BaseModel)
        self.assertEqual(type(stt.id), str)
        # datetime check
        self.assertEqual(type(stt.created_at), datetime)
        self.assertEqual(type(stt.updated_at), datetime)
        # name check
        self.assertTrue(hasattr(stt, "name"))
        self.assertEqual(type(stt.name), str)

#!/usr/bin/python3
"""Unittest for user"""
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """class tests for user"""

    def test_doc(self):
        """check docstring"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)

    def test_user(self):
        """tests for user"""
        userr = User()
        self.assertEqual(type(userr), User)
        self.assertEqual(type(userr.id), str)
        # datetime check
        self.assertEqual(type(userr.created_at), datetime)
        self.assertEqual(type(userr.updated_at), datetime)
        self.assertEqual(type(userr.first_name), str)
        self.assertEqual(type(userr.last_name), str)
        self.assertEqual(type(userr.email), str)
        self.assertEqual(type(userr.password), str)
        # check str
        self.assertEqual(type(userr.__str__()), str)
        self.assertNotEqual(len(userr.__str__()), 0)

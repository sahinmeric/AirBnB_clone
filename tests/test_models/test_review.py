#!/usr/bin/python3

"""Unittest for review"""
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """class tests for review"""

    def test_doc(self):
        """check docstring"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.save.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)
        self.assertIsNotNone(Review.__str__.__doc__)

    def test_type(self):
        """tests for review"""
        rvw = Review()
        self.assertEqual(type(rvw), Review)
        self.assertEqual(type(rvw.id), str)
        # datetime check
        self.assertEqual(type(rvw.created_at), datetime)
        self.assertEqual(type(rvw.updated_at), datetime)
        self.assertEqual(type(rvw.place_id), str)
        self.assertEqual(type(rvw.user_id), str)
        self.assertEqual(type(rvw.text), str)
        self.assertEqual(type(rvw.__str__()), str)
        self.assertNotEqual(len(rvw.__str__()), 0)

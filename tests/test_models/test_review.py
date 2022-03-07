#!/usr/bin/python3

"""Unittest for review"""
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """class tests for review"""

    def checkdocst(self):
        """check docstring"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.save.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)
        self.assertIsNotNone(Review.__str__.__doc__)

    def creatervw(self):
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
        self.assertEqual(type(rvw.name), str)

    def testsave(self):
        """test save method"""
        rvw1 = Review()
        createdat = rvw1.created_at
        updatedat = rvw1.updated_at
        #saving and testing
        rvw1.save()
        createdat2 = rvw1.created_at
        updatedat2 = rvw1.updated_at
        self.assertEqual(createdat, createdat2)
        self.assertNotEqual(updatedat, updatedat2)

    def teststore(self):
        """test storage"""
        rvw2 = Amenity()
        self.assertIn(rvw2, models.storage.all().values())

#!/usr/bin/python3
"""
Unittest for place_model
"""
import models
import unittest
from models.base_model import BaseModel
from models.place_model import Place


class TestPlace(unittest.TestCase):

    def checkdocst(self):
        """check docstring"""
        self.assertIsNotNone(Place.__doc__)

    def testplace(self):
        """check class and attrs"""
        pl = Place()
        self.assertIsInstance(pl, Place)
        self.assertIsInstance(pl, BaseModel)
        self.assertEqual(type(pl.created_at), datetime)
        self.assertEqual(type(pl.updated_at), datetime)
        self.assertTrue(hasattr(pl, "city_id"))
        self.assertEqual(type(pl.city_id), str)
        self.assertTrue(hasattr(pl, "user_id"))
        self.assertEqual(type(pl.user_id), str)
        self.assertTrue(hasattr(pl, "name"))
        self.assertEqual(type(pl.name), str)
        self.assertTrue(hasattr(pl, "description"))
        self.assertEqual(type(pl.description), str)
        self.assertTrue(hasattr(pl, "number_rooms"))
        self.assertEqual(type(pl.number_rooms), int)
        self.assertTrue(hasattr(pl, "number_bathrooms"))
        self.assertEqual(type(pl.number_bathrooms), int)
        self.assertTrue(hasattr(pl, "max_guest"))
        self.assertEqual(type(pl.max_guest), int)
        self.assertTrue(hasattr(pl, "price_by_night"))
        self.assertEqual(type(pl.price_by_night), int)
        self.assertTrue(hasattr(pl, "latitude"))
        self.assertEqual(type(pl.latitude), float)
        self.assertTrue(hasattr(pl, "longitude"))
        self.assertEqual(type(pl.longitude), float)
        self.assertTrue(hasattr(pl, "amenity_ids"))
        self.assertEqual(type(pl.amenity_ids), list)
        #check str
        self.assertEqual(str(pl), f'[Place] ({pl.id} \
                {pl.__dict__}')

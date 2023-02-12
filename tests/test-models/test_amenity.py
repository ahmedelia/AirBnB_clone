#!/usr/bin/python3
""" testing amenity model """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_amenity_creation(self):
        """ Test if Amenity instance is created correctly. """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_is_subclass(self):
        """ checking if subclass """
        amenity = Amenity()
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_attribute(self):
        """ Test if amenity name is set correctly. """
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_id(self):
        """ check id to ensure class inherits"""
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)

    if __name__ == '__main__':
        unittest.main()

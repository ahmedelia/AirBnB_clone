#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCaseCity(unittest.TestCase):
    """Test cases for City class."""

    def test_instance(self):
        """Test instantiation of City class."""
        city = City()
        self.assertIsInstance(city, City)

    def test_is_class(self):
        """Test type of City instance."""
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel."""
        city = City()
        self.assertTrue(issubclass(type(city), BaseModel))

    if __name__ == "__main__":
        unittest.main()

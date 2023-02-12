#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestCasePlace(unittest.TestCase):

    def test_instance(self):
        """ checking instance type """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_is_class(self):
        """ check if its a class """
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")

    def test_is_subclass(self):
        """ check if its a subclass"""
        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_city_id(self):
        """ testing the city id """
        place = Place()
        place.city_id = "SF"
        self.assertEqual(place.city_id, "SF")

    def test_user_id(self):
        """ testing the user id"""
        place = Place()
        place.user_id = "123"
        self.assertEqual(place.user_id, "123")

    def test_name(self):
        """ testing the place name """
        place = Place()
        place.name = "Place 1"
        self.assertEqual(place.name, "Place 1")

    def test_description(self):
        """ testing the description """
        place = Place()
        place.description = "A place to stay in SF"
        self.assertEqual(place.description, "A place to stay in SF")

    def test_number_rooms(self):
        """ testing the room numbers """
        place = Place()
        place.number_rooms = 2
        self.assertEqual(place.number_rooms, 2)

    def test_number_bathrooms(self):
        """ testing number of bathrooms """
        place = Place()
        place.number_bathrooms = 2
        self.assertEqual(place.number_bathrooms, 2)

    def test_max_guest(self):
        """ testing max guest users """
        place = Place()
        place.max_guest = 4
        self.assertEqual(place.max_guest, 4)

    def test_price_by_night(self):
        """ testing price by night """
        place = Place()
        place.price_by_night = 100
        self.assertEqual(place.price_by_night, 100)

    def test_latitude(self):
        """ testing latitude """
        place = Place()
        place.latitude = 37.7749
        self.assertEqual(place.latitude, 37.7749)

    def test_longitude(self):
        """ testing longitude """
        place = Place()
        place.longitude = -122.4194
        self.assertEqual(place.longitude, -122.4194)

    def test_amenity_ids(self):
        """ testing the amenity ids"""
        place = Place()
        place.amenity_ids = [1, 2, 3, 4]
        self.assertEqual(place.amenity_ids, [1, 2, 3, 4])
        self.assertIsNotNone(place.id)

        if __name__ == '__main__':
            unittest.main()

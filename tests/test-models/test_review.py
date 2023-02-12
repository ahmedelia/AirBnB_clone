#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestCaseReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_instance(self):
        """Test creating an instance of Review"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_is_class(self):
        """Test if Review is a class"""
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_place_id(self):
        """Test if place_id can be set and retrieved correctly"""
        review = Review()
        self.assertEqual(review.place_id, "")
        review.place_id = "fred123"
        self.assertEqual(review.place_id, "fred123")

    def test_user_id(self):
        """Test if user_id can be set and retrieved correctly"""
        review = Review()
        self.assertEqual(review.user_id, "")
        review.user_id = "shema123"
        self.assertEqual(review.user_id, "shema123")

    def test_text(self):
        """Test if text can be set and retrieved correctly"""
        review = Review()
        self.assertEqual(review.text, "")
        review.text = "This is a great place!"
        self.assertEqual(review.text, "This is a great place!")


if __name__ == "__main__":
    unittest.main()

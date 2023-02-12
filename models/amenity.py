#!/usr/bin/python3
"""
    the module thats contain
    amenityy class of airbnb project
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class for all amenity in proj
    just text to check if the comments is the prob
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Set up an instance with its properties. """
        super().__init__(*args, **kwargs)

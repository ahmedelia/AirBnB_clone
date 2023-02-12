#!/usr/bin/python3
"""
    the module thats contain
    amenityy class of airbnb project
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class for all amenity in proj"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

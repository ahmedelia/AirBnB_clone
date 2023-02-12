#!/usr/bin/python3
"""
    the module thats contain
    Place class of airbnb project
"""
from .base_model import BaseModel


class Place(BaseModel):
    """Place Class that conatin description and name and etc for proj
    just text to check if the comments is the prob
    """
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

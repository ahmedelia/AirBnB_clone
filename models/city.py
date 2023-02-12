#!/usr/bin/python3
"""
    the module thats contain
    city class of airbnb project
"""
from .base_model import BaseModel


class City(BaseModel):
    """City Class to store all cities in proj
    just text to check if the comments is the prob
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ Set up an instance with its properties. """
        super().__init__(*args, **kwargs)

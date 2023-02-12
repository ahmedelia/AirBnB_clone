#!/usr/bin/python3
"""
    the module thats contain
    city class of airbnb project
"""
from .base_model import BaseModel


class City(BaseModel):
    """City Class to store all cities in proj"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

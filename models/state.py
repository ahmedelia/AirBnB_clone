#!/usr/bin/python3
"""
    the module thats contain
    state class of airbnb project
"""
from .base_model import BaseModel


class State(BaseModel):
    """State Class to store state of curr
    just text to check if the comments is the prob
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Set up an instance with its properties. """
        super().__init__(*args, **kwargs)

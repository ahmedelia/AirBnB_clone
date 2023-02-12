#!/usr/bin/python3
"""
    the module thats contain
    state class of airbnb project
"""
from .base_model import BaseModel


class State(BaseModel):
    """State Class to store state of curr """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

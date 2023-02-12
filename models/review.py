#!/usr/bin/python3
"""
    the module thats contain
    Review class of airbnb project
"""
from .base_model import BaseModel


class Review(BaseModel):
    """Review Class store all # REVIEWs in proj
    just text to check if the comments is the prob
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

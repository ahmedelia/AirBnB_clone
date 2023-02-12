#!/usr/bin/python3
"""
    the module thats contain
    user class of airbnb project
"""
from .base_model import BaseModel


class User(BaseModel):
    """User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

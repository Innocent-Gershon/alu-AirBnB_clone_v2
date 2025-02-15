#!/usr/bin/python3
"""
This module contains Review class (Blueprint for creating Review objects).
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is the review class

    Attributes:
        place_id (str): The place id
        user_id (str): The user id
        text (str): The text of the review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

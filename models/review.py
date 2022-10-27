#!/usr/bin/env python3
from models.base_model import BaseModel
"""class represent review"""
class Review(BaseModel):
    """Review class inherits from superclass BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
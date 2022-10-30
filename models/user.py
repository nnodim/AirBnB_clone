#!/usr/bin/env python3
from models.base_model import BaseModel
"""class represent user"""


class User(BaseModel):
    '''User class instance of BaseModel class'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

# -*- coding: utf-8 -*-
# app/models/utils.py

"""utils.py

This module implements functions for 
key generation and password verification.
"""

from uuid import uuid1
from hashlib import md5

def generate_key():

    return str(uuid1())

def hash_password(password):

    _hash = md5(password.encode())

    return _hash.hexdigest()

def verify_password(_hash, password):

    return _hash == hash_password(password)
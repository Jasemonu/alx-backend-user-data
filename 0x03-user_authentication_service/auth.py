#!/usr/bin/env python3
"""A method for hashing users passwords"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from typing import Union


def _hash_password(password: str) -> str:
    """Hashing password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    def __init__(self):
        """Authentication class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[None, User]:
        """User registration method"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            # User not found, proceed with registration

            return self._db.add_user(email, _hash_password(password))
        else:
            # if user already exists, throw error
            raise ValueError('User {} already exists'.format(email))

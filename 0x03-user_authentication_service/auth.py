#!/usr/bin/env python3
"""A method for hashing users passwords"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
# from uuid import uuid4

from typing import TypeVar


def _hash_password(password: str) -> str:
    """Hashing password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Instanciating DB"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """return a User object."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        raise ValueError('User {} already exists'.format(email))

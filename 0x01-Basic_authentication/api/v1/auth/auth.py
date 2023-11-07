#!/usr/bin/env python3
"""API authentication class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """manages API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None"""
        return None

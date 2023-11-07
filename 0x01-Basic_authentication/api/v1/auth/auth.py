#!/usr/bin/env python3
"""API authentication class
"""

from flask import request
from typing import List, TypeVar

class Auth:
    """A public method"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def current_user(self, request=None) -> TypeVar('User'):
        return None




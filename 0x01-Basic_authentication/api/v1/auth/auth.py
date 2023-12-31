#!/usr/bin/env python3
"""API authentication class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """manages API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method, checks if authentication is required"""
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        if request and request.headers.get('Authorization'):
            return request.headers['Authorization']
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None"""
        return None

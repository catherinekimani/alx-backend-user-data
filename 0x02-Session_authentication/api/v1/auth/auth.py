#!/usr/bin/env python3
""" Auth class """
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if authentication is required for a given path """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path.rstrip('/') + '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path.rstrip('*')):
                    return False
            elif path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Request validation! """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ get current user """
        return None

    def session_cookie(self, request=None):
        """ Return a coolie value from a request """
        if request is None:
            return None
        session_cookie_name = os.getenv('SESSION_NAME', ' _my_session_id')
        session_id = request.cookies.get(session_cookie_name)
        return session_id

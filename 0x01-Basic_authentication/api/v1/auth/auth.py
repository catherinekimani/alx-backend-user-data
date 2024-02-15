#!/usr/bin/env python3
""" Auth class """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if authentication is required for a given path """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ Request validation! """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ get current user """
        return None

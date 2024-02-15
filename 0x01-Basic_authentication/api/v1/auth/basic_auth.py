#!/usr/bin/env python3
""" Basic auth """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication Class """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication:
        """
        if authorization_header is None or not isinstance(
            authorization_header, str
        ):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        R_base64 = authorization_header.split(' ')[1]
        return R_base64

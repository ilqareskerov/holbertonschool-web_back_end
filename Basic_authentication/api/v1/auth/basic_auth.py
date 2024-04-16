#!/usr/bin/env python3
'''
manage the API authentification
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        ''' def decode base64 authorization header '''
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            return base64_authorization_header.encode('utf-8').decode('base64')
        except Exception:
            return None

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' def extract base64 authorization header '''
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith("Basic "):
            return "".join(authorization_header.split(" ")[1:])

#!/usr/bin/env python3
'''
manage the API authentification
'''
from flask import request
from typing import List, TypeVar


class Auth:
    """
manage the API authentification
"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' require_authentification '''
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if path is None or excluded_paths is None:
            return True
        path = path + '/' if path[-1] != '/' else path
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None

    def session_cookie(self, request=None):
        '''self descriptive'''
        if not request:
            return None

        session_name = os.getenv("SESSION_NAME")
        return request.cookies.get(session_name)

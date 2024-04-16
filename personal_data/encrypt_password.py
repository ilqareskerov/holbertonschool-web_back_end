#!/usr/bin/env python3
'''hash password'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''returns the SHA256 hash of a password'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

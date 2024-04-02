#!/usr/bin/env python3
""""
a type-annotated function floor which takes a float n as argument and returns the floor of the float."""

def floor(n:float)->int: 
    """Returns the largest integer less than or"""
    if n < 0:
        return int(n)-1
    return int(n)

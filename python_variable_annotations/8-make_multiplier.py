#!/usr/bin/env python3
'''
Write a type-annotated function sum_list
which takes a list input_list of floats as
argument and returns their sum as a float.
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a new function that multip'''
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function

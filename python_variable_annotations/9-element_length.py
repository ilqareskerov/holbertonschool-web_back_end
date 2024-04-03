#!/usr/bin/env python3
'''
Write a type-annotated function sum_list
which takes a list input_list of floats as
argument and returns their sum as a float.
'''

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from the input list
    along with its length.
    
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.
        
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains an element
        from the input list along with its length.
    """
    return [(i, len(i)) for i in lst]

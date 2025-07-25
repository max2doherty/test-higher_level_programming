#!/usr/bin/python3
"""function that adds 2 integers.
    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, otherwise raise a TypeError exception
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
"""

def add_integer(a, b=98):
    """
        add_integer function adds two numbers
        args a: an int or a float
            b: an int or a float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    try:
        a = int(a)
    except OverflowError:
        raise OverflowError("a is too large to convert to an integer")

    try:
        b = int(b)
    except OverflowError:
        raise OverflowError("b is too large to convert to an integer")
    
    return int(a) + int(b)

#!/usr/bin/python3
def add_integer(a, b=98):
    """
        add_integer function adds two numbers
        args a: an int or a float
            b: an int or a float
        Returns:
            int: The sum of a and b, both cast to integers.

         Raises:
             TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

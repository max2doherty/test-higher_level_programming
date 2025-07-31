#!/usr/bin/python3
"""write a function that prints a square with the character #"""


def print_square(size):
    """prints a square
        arguments
            size: the size of the square
        return: a square of size size is printed
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

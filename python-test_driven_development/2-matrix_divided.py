#!/usr/bin/python3
"""write a function thats divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides a matrix
        arguments
            matrix: a list containing rows of integers
            div: a number that divides each element
        return: a matrix of the results is returned
        """
    reference_length = len(matrix[0])
    for row in matrix:
        if len(row) != reference_length:
            raise TypeError("Each row of the matrix must have the same size")
    new = []
    new_row = []
    for row in matrix:
        new = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            a = round(i / div, 2)
            new.append(a)
        new_row.append(new)
    return new_row

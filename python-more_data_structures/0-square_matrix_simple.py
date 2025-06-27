#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        temp_row = []
        for i in row:
            temp_row.append(i ** 2)
        result_matrix.append(temp_row)
    return result_matrix

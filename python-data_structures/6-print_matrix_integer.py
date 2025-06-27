#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        temp_row = []
        for i in row:
            temp_row.append("{}".format(i))
        print(" ".join(temp_row))

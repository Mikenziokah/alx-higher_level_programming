#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = matrix.copy()
    for a in range(len(matrix)):
        my_matrix[a] = list(map(lambda x: x **2, matrix[a]))
        return (my_matrix)

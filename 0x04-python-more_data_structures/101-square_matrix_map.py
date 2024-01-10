#!/usr/bin/python3
def square_matrix_map(matrix=[]):

    """
    square_matrix_map:
        function that computes the square value
        of all integers of a matrix using map.

    arugments:
        square: is the square matrix
        matrix: is a 2 dimensional array
        map: is the map of the matrix

    Return:
        Same size as matrix
        Each value should be the square of the value of the input
    """
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))

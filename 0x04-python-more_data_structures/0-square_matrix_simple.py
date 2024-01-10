#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    """
    square_matrix_simple:
        function that computes the square value of all integers of a matrix.

    Args:
        matrix: the list of the square
        is a 2 dimensional array

    Returns:
        Same size as matrix
        Each value should be the square of the value of the input
        new matrix or None if null
    """
    if len(matrix) == 0 or matrix is None:
        return (None)
    new_matrix = []
    for each in matrix:
        new_matrix.append([x ** 2 for x in each])
    return (new_matrix)

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    """print_matrix_integer:
        function that print a matrix of integer.

    Args:
        matrix: the element that contain the list

    Returns:
        NULL
    """
    if len(matrix) == 0 or matrix is None:
        return (None)
    for p in range(len(matrix)):
        for q in range(len(matrix[p])):
            if q == len(matrix[p]) - 1:
                print("{:d}".format(matrix[p][q]))
            else:
                print("{:d}".format(matrix[p][q]), end=' ')

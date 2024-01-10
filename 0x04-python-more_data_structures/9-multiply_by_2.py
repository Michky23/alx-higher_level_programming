#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    """
    multiply_by_2:
        function that returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: a dictionary

    Returns:
       a new dictionary with modified value
    """
    new_dict = {}
    for p in a_dictionary:
        new_dict[p] = a_dictionary[p] * 2
    return (new_dict)

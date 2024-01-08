#!/usr/bin/python3
def max_integer(my_list=[]):

    """
    max_integer:
        function that finds the biggest integer of a list

    Args:
        my_list: the list that contains the integers

    Returns:
        none, if list is empty
    """
    if len(my_list) == 0:
        return (None)
    min_value = -10000000
    for p in my_list:
        if p > min_value:
            min_value = p
    return (min_value)

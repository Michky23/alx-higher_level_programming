#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    """
    divisible_by_2:
        function that finds all multiples of 2 in a list.

    Args:
        my_list: the list of integer

    Returns:
        a new list with True or False
        return the bool value of result
    """
    new_list = []
    for p in my_list:
        new_list.append(p % 2 == 0)
    return (new_list)

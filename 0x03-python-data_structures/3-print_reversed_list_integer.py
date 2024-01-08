#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print_reversed_list_integer:
        function that prints all integers of a list, in reverse order.

    Argments:
        my_list: the list to reverse

    Returns:
        Null
    """
    if my_list is None:
        return ('')
    if len(my_list) == 0:
        return ('')
    for p in range(int(len(my_list) / 2)):
        idx = len(my_list) - p - 1
        element = my_list[idx]
        my_list[idx] = my_list[p]
        my_list[p] = element
    for p in my_list:
        print("{:d}".format(p))

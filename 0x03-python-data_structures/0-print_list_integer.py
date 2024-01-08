#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print integer in the list

    Args:
        my_list: the list to print from

    Returns:
        NULL
    """
    for p in my_list:
        print("{:d}".format(p))

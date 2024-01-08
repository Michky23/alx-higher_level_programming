#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific position.

    Arguments:
        my_list: the element of the list
        idx: the index of the list
        element: the element to put at the index

    Returns:
        the original list
        the new list with modified element if found
        else return null if idx < 0 or > list
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    my_list[idx] = element
    return (my_list)

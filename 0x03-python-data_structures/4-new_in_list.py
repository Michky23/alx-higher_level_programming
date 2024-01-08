#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """new_in_list:
        function that replaces an element in a list at a specific
        position without modifying the original list (like in C).

    Argments:
        my_list: the list to modify
        idx: the index of the list
        element: the element to modify

    Returns:
        copy of the original list
        the new_list or org_list if idx < 0 or
        out of range
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list.copy())
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)

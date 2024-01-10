#!/usr/bin/python3
def search_replace(my_list, search, replace):

    """
    search_replace:
        function that replaces all occurrences of an element
        by another in a new list.

    Args:
        my_list: is the initial list
        search: is the element to replace in the list
        replace: is the new element

    Returns:
        the new list with replace element
    """
    new_list = []
    if my_list is None:
        return (None)
    if len(my_list) == 0:
        return ([])
    for p in my_list:
        if p == search:
            new_list.append(replace)
        else:
            new_list.append(p)
    return (new_list)

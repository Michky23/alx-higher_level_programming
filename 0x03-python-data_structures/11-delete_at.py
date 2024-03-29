#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    """
    delete_at:
        function that deletes the item at a specific position in a list.

    Args:
        my_list: the list to delete from
        idx: the index to remove from

    Returns:
        the same list, new list or old list if error
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    del my_list[idx]
    return (my_list)

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    """
    only_diff_elements:
        function that returns a set of all elements present in only one set.

    Args:
        set_1: the first set
        set_2: the second set

    Returns:
        the difference between two sets
    """
    if set_1 is None or set_2 is None:
        return (None)
    return (set_1 ^ set_2)

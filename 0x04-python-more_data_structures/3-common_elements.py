#!/usr/bin/python3
def common_elements(set_1, set_2):

    """
    common_elements:
        function that returns a set of common elements in two sets.

    Args:
        set1: the first se
        set2: the second set

    Returns:
        the common element in the two sets
    """
    if set_1 is None or set_2 is None:
        return (None)
    return (set_1 & set_2)

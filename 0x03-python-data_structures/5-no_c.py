#!/usr/bin/python3
def no_c(my_string):
    """no_c:
        function that removes all characters c and C from a string.

    Args:
        my_string: the string list

    Returns:
        the new string without c and C
    """
    new_string = ''
    for p in range(len(my_string)):
        if my_string[p] not in 'cC':
            new_string += my_string[p]
    return (new_string)

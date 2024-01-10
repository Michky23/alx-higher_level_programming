#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """complex delete in a dictionary

    Args:
        a_dictionary: the dictionary
        value in the dictionary

    Returns:
        the dictionary with change value
    """
    new_list = []
    for p, o in a_dictionary.items():
        if o == value:
            new_list.append(p)
    for n in new_list:
        del a_dictionary[n]
    return (a_dictionary)

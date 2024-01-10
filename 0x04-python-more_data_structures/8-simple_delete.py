#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):

    """
    simple_delete:
        function that deletes a key in a dictionary.

    Argments:
        a_dictionary: the dictionary
        key: the key, argument will be always a string

    Returns:
       return the new dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)

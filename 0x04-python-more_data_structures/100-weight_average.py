#!/usr/bin/python3
def weight_average(my_list=[]):

    """
    weight_average:
        function that returns the weighted average of all
        integers tuple (<score>, <weight>)

    Args:
        my_list: the list

    Returns:
        0 if the list is empty
    """
    new_list = []
    count = 0
    if len(my_list) == 0:
        return (0)
    for w in my_list:
        new_list.append(w[0] * w[1])
        count += w[1]
    return (sum(new_list) / count)

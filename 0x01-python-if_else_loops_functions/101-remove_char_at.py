#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ''
    for p in range(len(str)):
        if p == n:
            continue
        else:
            newstr = newstr + str[p]
    return (newstr)

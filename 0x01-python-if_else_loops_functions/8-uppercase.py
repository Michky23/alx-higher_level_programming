#!/usr/bin/python3
def uppercase(str):
    newstr = ''
    for p in range(len(str)):
        if ord(str[p]) in range(97, 123):
            newstr = newstr + chr(ord(str[p]) - 32)
        else:
            newstr = newstr + str[p]
    print("{}".format(newstr))

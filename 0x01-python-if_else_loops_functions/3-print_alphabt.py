#!/usr/bin/python3
for p in range(97, 123):
    if chr(p) == 'q' or chr(p) == 'e':
        continue
    print("{}".format(chr(p)), end="")

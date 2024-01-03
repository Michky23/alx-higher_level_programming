#!/usr/bin/python3
for p in range(0, 100):
    if p == 99:
        print(99)
        break
    print("{:02d}, ".format(p), end="")

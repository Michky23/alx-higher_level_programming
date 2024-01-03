#!/usr/bin/python3
for p in range(0, 10):
    for q in range(p + 1, 10):
        if p != 0 or q != 1:
            print(", {:02d}".format(p * 10 + q), end="")
        else:
            print("{:02d}".format(p * 10 + q), end="")
print()

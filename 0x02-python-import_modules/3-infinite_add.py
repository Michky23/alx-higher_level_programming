#!/usr/bin/python3

if __name__ == "__main__":
    """add infinite numbers on CLD arg"""
    import sys

    argv = sys.argv
    b = len(argv) - 1
    sum = 0
    if b == 0:
        print(sum)
    else:
        for p in range(1, len(argv)):
            sum += int(argv[p])
        print(sum)

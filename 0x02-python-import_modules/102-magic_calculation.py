#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    """magic calculation challenge 3"""
    if a < b:
        z = add(a, b)
        for p in range(4, 6):
            z = add(z, p)
        return (z)
    else:
        return (sub(a, b))

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p = 0
if number < 0:
    p = -(-number % 10)
else:
    p = number % 10
print("Last digit of {} is {} and is ".format(number, p), end="")
if p > 5:
    print("greater than 5")
elif p == 0:
    print('0')
else:
    print('less than 6 and not 0')

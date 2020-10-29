"""
reduce: a list of items reduce to one item
r = reduce(function, sequence)
"""
from functools import reduce


def add(x, y):
    return x + y


x = reduce(add, range(1, 101))
print(x)

x = reduce(lambda x, y: x + y, [47,11,42,13])
print(x)
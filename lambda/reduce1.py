"""find maximum or minimum"""
from functools import reduce

max = lambda a, b: a if (a > b) else b
x = reduce(max, [47, 11, 42, 102, 13])
print("max =", x)

min = lambda a, b: a if (a < b) else b
x = reduce(min, [47, 11, 42, 102, 13])
print("min =", x)

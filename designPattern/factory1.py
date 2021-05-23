"""
understand "globals()"
"""
from pprint import pprint

class Dog:
    def __init__(self, name):
        self.name = name

a = 100
b = 4

def foo():
    x = 100 # x is a local variable

pprint(globals())
pprint(globals()["Dog"])
pprint(globals()["Dog"]("Lucky"))

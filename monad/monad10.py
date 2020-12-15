"""
bind list function
"""
from pymonad.operators.maybe import Just, Nothing
from pymonad.list import *

def neg(x):
    return ListMonad(-x)

def add3(x):
    return ListMonad(x+3)

x= Just(7).bind(neg).bind(add3)
print("11:",x)

x = ListMonad(2,3).bind(neg).bind(add3)
print("14:",x)

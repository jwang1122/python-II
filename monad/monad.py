from pymonad.operators.maybe import Just
from pymonad.tools import curry

def add3(number):
    return Just(number + 3)

def mul4(number):
    return Just(number * 4)

x = Just(2) >> add3 >> mul4
print(x)

def f1(number):
    return Just(number) >> add3 >> mul4

x = f1(11)
print(x)

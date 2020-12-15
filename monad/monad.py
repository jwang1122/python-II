from pymonad.operators.maybe import Just
from pymonad.tools import curry

def add3(number):
    return Just(number + 3)

def mul4(number):
    return Just(number * 4)

def half(number):
    return Just(number/2)

x = Just(2) >> add3 >> half #链式运行结构
print(x)

def f1(number):
    return Just(number) >> add3 >> mul4 >> half

x = f1(11)
print(x)

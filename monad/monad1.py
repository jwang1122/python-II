"""
Just: boxed value
Functor: operate a founction to a boxed value
"""
from pymonad.operators.maybe import Just
from pymonad.tools import curry

# Functor "Just" implements fmap
@curry(1)
def sayHello(person):
    return f"Hello, {person}!"

print("13",sayHello(None))
print("14:", sayHello("John"))
print("15:", sayHello(Just("World")))
print("16:",type(sayHello(Just("World"))))
print("17:", sayHello * Just("World")) # Just是一个Functor，implement fmap功能块，使得普通的功能块可以使用*作用其上
print("18:",type(sayHello * Just("World")))
print("19:", sayHello * Just(None))
x = Just("Wang").map(sayHello)
print("21:",x)

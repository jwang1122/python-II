from pymonad.tools import curry
from pymonad.operators.maybe import Just, Nothing
from pymonad.list import *

def positive_and_negative(x):
    return ListMonad(x, -x)

@curry(2)
def add_and_sub(x, y): #curry make it possible to do applicative send variable one at a time.
    return ListMonad(y + x, y - x)

# Monads allow you to sequence a series of calculations within than monad using the bind operator >>.
x = ListMonad(2,3).bind(positive_and_negative)
print("14:",x)
x = ListMonad(2,3).bind(positive_and_negative).bind(add_and_sub(3))  #链式运行结构
#2+3, 2-3, -2+3, -2-3, 3+3, 3-3, 3+-3, 3--3 
print("17:",x)

x = Just(4).bind(positive_and_negative).bind(add_and_sub(3))  #链式运行结构
print("20:",x)

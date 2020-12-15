from pymonad.operators.maybe import Just
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return x + y

add3 = add * Just(3) 
print(add3)
wrapperedValue = add3 & Just(2) # applicative apply function to a wrapped number
print(wrapperedValue)

x = add * Just(3) & Just(2)
print(x)
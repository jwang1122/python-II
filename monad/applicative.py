"""
Think about you have a large function used quite long time;
You need add additional arguments to it,
but you don't want make code change on existing function call.

Applicative functors are a construction that provides the midpoint 
between functors and monads, and are therefore more widespread than monads, 
while more useful than functors. Normally you can just map a function over a functor. 
Applicative functors allow you to take a "normal" function (taking non-functorial arguments) 
use it to operate on several values that are in functor contexts.
 As a corollary, this gives you effectful programming without monads.
"""
from pymonad.operators.maybe import Just
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return x + y

x = add * Just(3) & Just(2)
print("Appy function to wrappered value one at a time...")
print(x)

print()
add3 = add * Just(3) 
print("Wrappered function: ")
print(add3)

wrapperedValue = add3 & Just(2) # applicative apply function to a wrapped number
print("Apply wrappered function to next argument...")
print(wrapperedValue)


print()
@curry(3)
def math1(a, b, c):
    return a + b - c

x = math1 * Just(10) & Just(3) & Just(5) # Reactive X way to call function
print("More then two arguments")
print(x)

try:
    x = math1 * Just(10) & Just(None) & Just(5)
    print(x)
except TypeError as te:
    print(te)
print("Done.")
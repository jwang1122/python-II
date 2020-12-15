from pymonad.operators.maybe import *
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return Maybe(x + y, True)

@curry(2)
def div(x, y):
    if y==0:
        return Nothing
    return Maybe(x / y, True)

@curry(2)
def mul(x, y):
    return Maybe(x * y, True)

a=10
b=7
c=3
d=5
m = (Maybe.insert(a).then(add(b)).then(div(c)).then(mul(d)).option(0, lambda x: x))
print(m)

c=0
m = (Just(a).then(add(b)).then(div(c)).then(mul(d)).maybe(0, lambda x: x))
print(m)

m = div(10, c)
print(m)

m = Maybe.insert(a)
print(m)

print("Done.")
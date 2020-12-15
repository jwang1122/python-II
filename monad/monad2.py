from pymonad.tools import curry
from pymonad.operators.maybe import Just

@curry(2)
def add(x, y):
    return x + y

@curry(2)
def mul(x, y):
    return x * y

print(add(2, 3))
print(mul(2,3))

# 最终目的是要连续执行的形式。
add2 = add * Just(2) & Just(8) # Applicative
print(add2)

mul2 = mul * Just(5) & Just(9)
print(mul2)


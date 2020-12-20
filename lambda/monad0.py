from pymonad.operators.maybe import Maybe, Just, Nothing
from pymonad.either import *
from pymonad.tools import curry

def mdiv(a, b):
    if b == 0:
        return Nothing
    return (a / b)

# @do(Maybe)
def with_maybe(first_divisor):
    val1 = yield mdiv(2.0, 2.0)
    val2 = yield mdiv(3.0, 0.0)
    val3 = yield mdiv(val1, val2)
    mreturn(val3)

x = with_maybe(12)
print(x.value)

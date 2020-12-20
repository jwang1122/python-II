from pymonad.tools import kleisli_compose
from pymonad.operators.maybe import Maybe, Just, Nothing

# any input is 0 will return Nothing instead of None
# Nothing: Maybe[Any] = Maybe(None, False), Wrapper of None.
def fail_if_zero(x):
    return Nothing if x==0 else Just(x)

def add1(x):
    return Just(x + 1)

if __name__ == '__main__':
    new_function = kleisli_compose(add1, fail_if_zero)
    print(new_function(0)) # returns Just(1)
    print(new_function(-1)) # returns Nothing


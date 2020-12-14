from pymonad.reader import Compose

def add_1(x):
    return x + 1

def mul_3(x):
    return 3 * x

# Creates a new function that first adds 1, then multiplies by 3, and
# finally converts the result to a string.
new_func = (Compose(add_1)
            .then(mul_3)
            .then(str)
)

print(new_func(2)) # '9'
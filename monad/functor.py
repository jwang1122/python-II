from pymonad.operators.maybe import Just

def add3(number):
    return number + 3

def mul4(number):
    return number * 4

x = add3 * Just(2)
print(x)

x = mul4 * (add3 * Just(2))
print(x)

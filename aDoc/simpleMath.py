"""
Simple Math functions add(), sub(), mul(), div(). 
There is no any type check for all functions which may cause unexpected result.

"""
def add(x, y, /):
    """
    Simple add() function with 2 positional arguments.

    Usage: z = add(10, 30)

    return: sum of two input numbers.
    """
    return x + y


def sub(x, y, /):
    return x - y


def mul(x, y, /):
    return x * y


def div(x, y, /):
    return x / y

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    if y == 0:
        raise ZeroDivisionError("The divisor is 0.")
    return x / y

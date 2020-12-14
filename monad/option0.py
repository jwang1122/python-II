from mymonad import *


def divide(x, y):
    if y == 0:
        return Nil()
    return Some(x / y)


if __name__ == "__main__":
    v = divide(10, 3)
    if v.defined:
        print(v.value)
    v = divide(10, 0)
    if v.defined:
        print(v.value)
    else:
        print("the result is undefined")
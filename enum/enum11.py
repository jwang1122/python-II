from enum import IntEnum, Enum
"""
IntEnum can be used as index of list or tuple
"""
class Color(Enum):
    RED = 1 # if the value is not important
    GREEN = 2 # must assign a value (int, str, ...)
    BLUE = 3

class Shapes(IntEnum):
    CIRCLE=1
    SQUARE=4
    HEXAGONE=6
    PENTAGON=6
    TRIANGLE=3

if __name__ == '__main__':
    x = Color.RED
    y = Shapes.CIRCLE
    print(x)
    print(y)
    print(x==y)
    l=['a','b','c']
    z=l[Color.RED.value]
    z1 = l[Shapes.CIRCLE]
    print(z==z1)
    print(z)
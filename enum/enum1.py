import enum

class Color(enum.Enum):
    RED = enum.auto # if the value is not important
    GREEN = 2 # must assign a value (int, str, ...)
    BLUE = 3

if __name__ == '__main__':
    print(Color.RED)
    print(repr(Color.RED))
    print(type(Color.BLUE))
    print(isinstance(Color.GREEN, Color))
    for color in Color:
        print(color)
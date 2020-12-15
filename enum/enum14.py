from enum import Enum, auto

class NoValue(Enum):
    def __str__(self):
        return '<%s.%s>' %(self.__class__.__name__, self.name)

class Color(NoValue):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    # RED = object()
    # BLUE = object()
    # GREEN = object()
    # RED = "stop"
    # BLUE = "too fast!"
    # GREEN = "go"

if __name__ == '__main__':
    print(Color.RED)
    for c in Color:
        print(c)
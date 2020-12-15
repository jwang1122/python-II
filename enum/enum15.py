from enum import Enum, auto

class NoValue(Enum):
    def __str__(self):
        return '<%s.%s>' %(self.__class__.__name__, self.name)

class AutoNumber(NoValue):
    """
    The major difference between __init__() and __new__() is 
    that __new__ handles object creation and 
    __init__ handles object initialization.
    """
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_=value
        return obj

class Color(AutoNumber):
    RED = ()
    GREEN = ()
    BLUE = ()

if __name__ == '__main__':
    print(type(Color.RED))
    print(Color.GREEN)
    print(Color.GREEN.value)
    for c in Color:
        print(c.value)
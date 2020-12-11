from enum import Enum, auto

"""
Enum with additional variable
"""


class NoValue(Enum):
    def __repr__(self):
        return "<%s.%s>" % (self.__class__.__name__, self.name)


class AutoNumber(NoValue):
    """
    The major difference between these two methods is
    that __new__ handles object creation and
    __init__ handles object initialization.
    """

    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class Swatch(AutoNumber):
    def __init__(self, pantone="unknown"):
        self.pantone = pantone

    AUBURN = "3497"
    SEA_GREEN = "1246"
    BLEACHED_CORAL = ()  # New color, no Pantone code yet!


if __name__ == "__main__":
    print(Swatch.SEA_GREEN.name)
    print(Swatch.SEA_GREEN.value)
    print(Swatch.SEA_GREEN.pantone)
    print(Swatch.BLEACHED_CORAL.pantone)

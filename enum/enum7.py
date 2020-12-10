from enum import Enum, auto
"""
make the value same as name automatically
"""
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

if __name__ == '__main__':
    print(list(Ordinal))

    for name, member in Ordinal.__members__.items():
        print(name, member)
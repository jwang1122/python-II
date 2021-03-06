from enum import Enum, auto

"""
make enum comparable
"""


class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class Grade(OrderedEnum):
    A = 5
    B = 4
    C = 3
    D = 2
    F = 1


if __name__ == "__main__":
    print(Grade.A > Grade.C)
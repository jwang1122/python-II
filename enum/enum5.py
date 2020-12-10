from enum import Enum, unique
"""
ValueError: duplicate values found in <enum 'Mistakes'>: FOUR -> THREE
"""
@unique
class Mistakes(Enum):
    ONE=1
    TWO=2
    THREE=3
    FOUR=3

if __name__ == '__main__':
    x = Mistakes.FOUR
    print(x)

import enum
"""
enum only allow unique key
TypeError: Attempted to reuse key: 'SQUARE'
"""
class Shape(enum.Enum):
    SQUARE=2
    SQUARE=4

if __name__ == '__main__':
    x = Shape.SQUARE
    print(x)
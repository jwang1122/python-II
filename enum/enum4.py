import enum
"""
same value causes only first key take effects
"""
class Shapes(enum.Enum):
    CIRCLE=1
    SQUARE=4
    RECTANGLE=4
    HEXAGONE=6
    PENTAGON=5
    TRIANGLE=3
    ALIAS_FOR_SQUARE=4

if __name__ == '__main__':
    x=Shapes.RECTANGLE
    print(x.name) # use key
    print(Shapes(4)) # use value find key
    print(Shapes.ALIAS_FOR_SQUARE)
    print(Shapes['PENTAGON']) # item slice

    print()
    for shape in Shapes: # ordered list
        print(shape)
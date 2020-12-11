from enum import Enum
"""
__new__() must be used whenever you want to customize 
the actual value of the Enum member. Any other modifications 
may go in either __new__() or __init__(), with __init__() 
being preferred.

For example, if you want to pass several items 
to the constructor, but only want one of them to be the value:
"""

class Coordinate(bytes, Enum):
    def __new__(cls, value, label, unit):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        obj.unit = unit
        return obj

    PX = (0, 'P.X', 'km')
    PY = (1, 'P.Y', 'km')
    VX = (2, 'V.X', 'km/s')
    VY = (3, 'V.Y', 'km/s')

if __name__ == '__main__':
    print(Coordinate)
    for x in Coordinate:
        print(x)
    x = Coordinate['VY'] # use key to get the enum
    print(x.label)
    print(x.unit)
    x = Coordinate(2) # use value to get the enum
    print(x.label)
    print(x.unit)
    
    
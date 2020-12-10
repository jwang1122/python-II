from enum import Enum

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
    x = Coordinate['VY']
    print(x.label)
    print(x.unit)
    x = Coordinate(2)
    print(x.label)
    print(x.unit)
    
    
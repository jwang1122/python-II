from math import pi
from level2.function.areaTable import areaTable
"""
重要的 web service 理念：
永远pass一个单一变量，返回一个单一变量。
例如：
    输入：ServiceRequest
    返回：ServiceResponse
"""
def circleArea(args):
    r = args[0]
    return r*r*pi

def squareArea(args):
    s = args[0]
    return s*s

def rectangleArea(args):
    width = args[0]
    height = args[1]
    return width*height

def triangleArea(args):
    side = args[0]
    height = args[1]
    return side*height/2

def unsupportedArea(mod):
    print("Unsupported area calculation mod: [%s] ..." %mod)
    return 0

def area(*args, mod="circle"):
    func = areaTable.get(mod, unsupportedArea)
    if func == unsupportedArea:
        return unsupportedArea(mod)
    return func(args)

if __name__ == '__main__':
    x = area(1)
    print("The circle area is %5.2f." %x)
    x = circleArea([2,])
    print(x)
    # mod is keyword argument only, if you don't provide the key, it will get into args array which is positional arguments.
    x = area(2, mod="square")
    print("The square area is %5.2f." %x)
    x = area(2.0, 3.5, mod="rectangle")
    print("The rectangle area is %5.2f." %x)
    x = area(2.0, 3.5, mod="triangle")
    print("The triangle area is %5.2f." %x)
    x = area(2.0, 3.5, mod="diamond")
    print("The diamond area is %5.2f." %x)


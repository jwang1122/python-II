from areaTable import *
"""
use decision table
"""
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


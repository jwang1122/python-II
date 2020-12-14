from math import pi

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

areaTable = {
    "circle":circleArea,
    "square":squareArea,
    "rectangle":rectangleArea,
    "triangle":triangleArea
}
import abc
from math import pi
"""
The abc module defines ABCMeta class which is a metaclass 
for defining abstract base class.

TypeError: Can't instantiate abstract class Shape with abstract method area
"""
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.length

class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * pi

if __name__ == '__main__':
    rectangle = Rectangle(10, 20)
    print("area: ", rectangle.area())
    circle = Circle(10)
    print("area: ", circle.area())
    s = Shape()
    print("area: ", s.area())

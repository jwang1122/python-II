import abc
from math import pi


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass


#class Rectangle(Shape):
class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.name = type(self).__name__

    def area1(self):
        return self.width * self.length


if __name__ == "__main__":
    rectangle = Rectangle(10, 20)
    print("area: ", rectangle.area1())
    print("Shape name: ", rectangle.name)

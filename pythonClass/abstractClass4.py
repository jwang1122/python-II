import abc
from math import pi
from student import Student

"""
AttributeError: 'Student' object has no attribute 'area'
How can I determine there is wrong instance passed to area() function at compiler time?

pip install mypy
(env) C:/Users/12818/workspace/python-II>mypy pythonClass/abstractClass4.py 
pythonClass/abstractClass4.py:48: error: Argument 1 to "area" has incompatible type "Student"; expected "Shape"
Found 1 error in 1 file (checked 1 source file)
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

def area(shape:Shape) -> float:
    return shape.area()

if __name__ == '__main__':
    rectangle = Rectangle(10, 20)
    print("area: ", rectangle.area())
    circle = Circle(10)
    print("area: ", circle.area())
    
    print(area(rectangle))
    print(area(circle))

    student = Student("Elle", 9, 13)
    print(area(student))
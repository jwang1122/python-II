"""
use factory to create instance with initial values.
"""
class Factory:
    def __init__(self, classname):
        self.classname = classname.capitalize()
    
    def getInstance(self):
        obj = globals()[self.classname]()
        return obj

class Area:
    def circleArea(self, r):
        from math import pi
        return pi * r * r

class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Teacher:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
 
class StudentFacroty:
    def __init__(self, classname = "Student"):
        self.classname = classname
    
    def getInstance(self, name):
        return globals()[self.classname](name)

if __name__ == '__main__':
    area_factory = Factory("area")
    print(type(area_factory))
    obj = area_factory.getInstance()
    area = obj.circleArea(1) 
    print(area)

    student_Facroty=StudentFacroty()
    s1 = student_Facroty.getInstance("John")
    print(type(s1))
    print(s1)

    teacher_factory=StudentFacroty("Teacher")
    t1 = teacher_factory.getInstance("John Wang")
    t1.occupation = "teacher"
    print(type(t1))
    print(t1)
    print(f"{t1} is a {t1.occupation}.")
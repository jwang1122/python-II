import abc
"""
Compare student by id and name
"""
# interface
class Comparable(abc.ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'compareTo') and 
                callable(subclass.compareTo) or 
                NotImplemented)

    @abc.abstractmethod
    def compareTo(self, object):
        raise NotImplementedError

class Student(Comparable):
    def __init__(self, id, name, grade, gender, age):
        self.id = id
        self.name = name
        self.grade = grade
        self.gender = gender
        self.age = age

    def compareTo(self, other):
        if self.id == other.id and self.name == other.name:
            return 0
        if self.id < other.id:
            return -1
        return 1

if __name__ == '__main__':
    s1 = Student(111,"John Wang", 7, "Male", 12)
    s2 = Student(111,"John Wang", 8, "Male", 13)
    s3 = Student(222,"David Johnson", 7, "Male", 12)
    print(s1.compareTo(s2))
    print(s1.compareTo(s3))
    
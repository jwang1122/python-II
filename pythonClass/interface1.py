import abc
"""
TypeError: Can't instantiate abstract class Student with abstract method compareTo
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
    pass

if __name__ == '__main__':
    s1 = Student()

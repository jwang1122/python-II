from observer import *

class Homework(ConcreteSubject):
    def assignHomework(self, homework):
        self.homework = homework
        self.notify()
        
    def __repr__(self):
        return self.homework

class Student(Observer):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def update(self, subject: Subject) -> None:
        print(f"{self.name} have received homework '{subject}' assignment" )

if __name__ == '__main__':
    s1 = Student(111,"John")
    s2 = Student(222, "David")
    s3 = Student(333, "Charles")
    h1 = Homework()
    h1.attach(s1)
    h1.attach(s2)
    h1.attach(s3)
    h1.assignHomework("Python1-20200706")
    h1.assignHomework("Python1-20200712")
    
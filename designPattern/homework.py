class Homework:
    def __init__(self):
        self.students = []
        self.homework = ""

    def notify(self):
        for s in self.students:
            s.receive(self.homework)

    def assignHomework(self, newHomework):
        self.homework = newHomework
        self.notify()

    def addStudent(self, student):
        self.students.append(student)

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def receive(self, homework):
        print(f"{self.name} have received homework '{homework}' assignment" )

if __name__ == '__main__':
    s1 = Student(111,"John")
    s2 = Student(222, "David")
    s3 = Student(333, "Charles")
    h1 = Homework()
    h1.addStudent(s1)
    h1.addStudent(s2)
    h1.addStudent(s3)
    h1.assignHomework("Python-20200706")
    h1.assignHomework("Python1-20200712")
    
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return "({0} grade={1} age={2})" \
            .format(self.name, self.grade, self.age)

    def increaseGrade(self):
        self.grade = self.grade + 1

s1=Student("John", 10, 13)
print("15:",s1)
s1.increaseGrade()
print("17:",s1)
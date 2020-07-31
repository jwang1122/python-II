from person import *

class student(person):
    def __init__(self, name, age, ssn, grade):
        super().__init__(name, age, ssn)
        self.grade = grade

    def increaseGrade(self):
        self.grade += 1
    
    def getGrade(self):
        return self.grade
    
    def getOccupation(self):
        print("I am a student...")

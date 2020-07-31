from student2 import *
from teacher import *

# student inherite from person
s1 = student("Bryan", 13, '999-99-9999',7)
print(s1)
print(s1.getGrade())
s1.increaseGrade()
print(s1.getGrade())

# teacher inherite from person
t1 = teacher("John", 45, "111-11-1111")
t1.assignHomework()

# Polymorphism
def printOccupation(p:person):
    p.getOccupation()

printOccupation(t1)
printOccupation(s1)
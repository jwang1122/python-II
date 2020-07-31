def avg(marks):
    assert len(marks) != 0, "List is empty!"
    return sum(marks)/len(marks)

mark1 = [2,3,6,1,23,45]
print("Average of mark1: %5.2f" %avg(mark1))

mark1 = []
print("Average of mark1: %5.2f" %avg(mark1))

print("Done.")
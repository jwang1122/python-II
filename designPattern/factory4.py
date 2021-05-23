class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class StudentFactory:
    def __init__(self, classname = "Student"):
        self.classname = classname
    
    def getInstance(self, **kwargs):
        obj = globals()[self.classname](kwargs['name'])
        return obj

if __name__ == '__main__':
    f1 = StudentFactory()
    s1 = f1.getInstance(name="John Wang")
    print(s1)
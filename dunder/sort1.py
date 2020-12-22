class Student():
    def __init__(self, id, name, grade, gender, age):
        self.id = id
        self.name = name
        self.grade = grade
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.id}-{self.name})"

    def __eq__(self, other):
        return self.id==other.id and self.name==other.name

    def __lt__(self, other):
        if self.id == other.id:
            if self.name < other.name:
                return True
            return False
        if self.id < other.id:
            return True
        return False

if __name__ == '__main__':
    s1 = Student(111,"John Wang", 7, "Male", 12)
    s2 = Student(222,"John Wang", 8, "Male", 13)
    s3 = Student(333,"David Johnson", 7, "Male", 12)
    s4 = Student(444,"Charles Johnson", 7, "Femal", 12)
    s5 = Student(555,"Linda Pang", 6, "Femal", 12)

    l = [s5, s3, s1, s2, s4]

    l1 = sorted(l, key=lambda x: x.name)
    print(l1)

    print(l)
    l.sort()
    print(l)

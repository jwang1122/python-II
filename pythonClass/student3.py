import csv


class Student:
    def __init__(self, id, firstname, lastname, score):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.score = score

    def __repr__(self):
        return f"({self.firstname} {self.lastname}, {self.score})"

    @classmethod
    def load(self, filename):
        self.students = []
        with open(filename, "r") as records:
            dictReader = csv.DictReader(records)
            for row in dictReader:
                s = Student(
                    row["id"], row["First name"], row["Last name"], row["Score"]
                )
                self.students.append(s)
        return self.students


if __name__ == "__main__":
    students = Student.load("class/students.csv")
    print(students)
from datetime import date

class User:
    def __init__(self, /, full_name="full name", birthdate="00011225"):
        self.full_name = full_name
        name_pieces = full_name.split(" ")

        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]
        yyyy = int(birthdate[0:4])
        mm = int(birthdate[4:6])
        dd = int(birthdate[6:8])
        self.birthday = (mm, dd)
        
        today = date.today()
        year = today.year
        self.age = year - yyyy
    
    def info(self):
        print(f"{self.full_name} is {self.age} years old.")
        print("His birthday is %d/%d" % self.birthday)

class SubUser(User):
    def getAge(self):
        return self.age

if(__name__ == "__main__"):
    john = SubUser("John Wang","19881122")
    john.info()
    print("{0} years old.".format(john.getAge()))
    print(f"{john.getAge()} years old.")
    ming=User()
    ming.info()
    print(type(ming))
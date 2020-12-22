class Person:
    def __init__(self, name, age, ssn):
        self.name = name
        self._age = age
        self.__ssn = ssn
    
    def __repr__(self):
        return "({0} age={1})".format(self.name, self._age)

    def getSSN(self, authority):
        if authority.isAuthorized():
            return self.__ssn
        return "Not authorized."

    def isAuthorized(self):
        return False

class Manager(Person):
    def isAuthorized(self):
        return True

if __name__ == '__main__':
    s1 = Person("Bryan", 13, '999-99-9999')
    print(s1)
    print(s1.name)
    try:
        print(s1.__ssn)
    except Exception as ex:
        print(ex)

    manager = Manager("John", 43, '999-99-9999')    
    print(s1.getSSN(manager))
    print(s1.getSSN(s1))

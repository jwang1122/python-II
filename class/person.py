class person:
    def __init__(self, name, age, ssn):
        self.name = name
        self.age = age
        self.ssn = ssn
    
    def __repr__(self):
        return "({0} age={1} ssn='{2}')".format(self.name, self.age, self.ssn)


    
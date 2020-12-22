import abc

class Person:
    def __init__(self, name, age, ssn):
        self.name = name
        self.age = age
        self.ssn = ssn
    
    def __repr__(self):
        return "({0} age={1} ssn='{2}')".format(self.name, self.age, self.ssn)

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'getOccupation') and 
                callable(subclass.getOccupation) or 
                NotImplemented)

    @abc.abstractmethod
    def getOccupation(self, object):
        raise NotImplementedError

if __name__ == '__main__':
    s1 = Person("Bryan", 13, '999-99-9999')
    print(s1)
    
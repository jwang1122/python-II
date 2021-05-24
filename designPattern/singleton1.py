"""
Singleton Pattern in Python:
1. private instance of the class
2. initialize the private instance in __init__
3. static function: getInstance() return the private instance, no self argument
"""


class Singleton:
    __instance = None  # private instance of the class
    classattribute = 5

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance == None:
            Singleton.__instance = self
        else:
            raise TypeError("Please use Singleton.getInstance().")

    @classmethod
    def getClassAttribute(cls):
        return cls.classattribute

    @classmethod
    def setClassAttribute(cls, value):
        cls.classattribute = value

if __name__ == "__main__":
    s1 = Singleton()
    print(s1)
    print(s1.getClassAttribute())
    try:
        s2 = Singleton()
        print(s2)        
    except Exception as error:
        print(error)
    s3 = Singleton.getInstance()
    Singleton.setClassAttribute(10)
    print(s3)
    print(Singleton.getClassAttribute())

    s4 = Singleton.getInstance()
    print(s4)
    print(s4.getClassAttribute())
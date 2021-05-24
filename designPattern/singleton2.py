"""
Singleton Pattern in Python:
1. private instance of the class
2. initialize the private instance in __init__
3. static function: getInstance() return the private instance, no self argument
"""


class Singleton:
    __instance = None  # private instance of the class
    classattribute = 5

    def __init__(self):
        self.instanceAttribute = "Hello world."
        if Singleton.__instance == None:
            Singleton.__instance = self
        else:
            raise TypeError("Please use Singleton.getInstance().")

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    @classmethod
    def getClassAttribute(cls):
        return cls.classattribute

    @classmethod
    def setClassAttribute(cls, value):
        cls.classattribute = value

    def getInstanceAttribute(self):
        return self.instanceAttribute

    def setInstanceAttribute(self, value):
        self.instanceAttribute = value

if __name__ == "__main__":
    s1 = Singleton()
    print(s1)
    print(s1.getClassAttribute())
    print(s1.getInstanceAttribute())
    
    try:
        s2 = Singleton()
        print(s2)        
        print(s2.getInstanceAttribute())       
    except Exception as error:
        print(error)

    s3 = Singleton.getInstance()
    print(s3)
    print(s3.getClassAttribute())
    print(s3.getInstanceAttribute())
    s3.setClassAttribute(100)
    s3.setInstanceAttribute("John Wang")

    s4 = Singleton.getInstance()
    print(s4)
    print(s4.getClassAttribute())
    print(s4.getInstanceAttribute())

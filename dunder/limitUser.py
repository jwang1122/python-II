from user import *

def thing1():
    print("I can run thing1.")

def thing2():
    print("I can run thing2.")

def thing3():
    print("I can run thing3.")

if __name__ == '__main__':
    user1 = User("John", 1111, ["thing1","thing3"])
    user2 = User("Bryan", 1122, ["thing2",])

    user1.do(thing1)
    user1.do(thing2)
    user2.do(thing2)

"""
under stand *args, after it, all keyword arguments must specifi the key.
"""
def myFunc(*args):
    for arg in args:
        print(arg, end=' ')
    print()

def myFunc1(*args, key="default key"):
    for arg in args:
        print(arg, end=' ')
    print()
    print(key)


if __name__ == '__main__':
    myFunc(1,2,4)
    myFunc1(1,2,3,"myKey")
    myFunc1(1,2,3,key="myKey")

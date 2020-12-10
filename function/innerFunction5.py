import random

def do_twice(func):  
    def wrapper_do_twice():  
        func()  
        func()  
    return wrapper_do_twice  

@do_twice  
def twoDices():  
    print( random.randint(1, 6))  

if(__name__ == "__main__"):
    twoDices()
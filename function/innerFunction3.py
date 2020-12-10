"""
Decorating function with arguments
"""
def divide(x,y):  
    print(x/y)  

def outer_div(func):  
    def inner(x,y):  
        if(x<y):  
            x,y = y,x  
            return func(x,y)  
    return inner  

if(__name__ == "__main__"):
    divide1 = outer_div(divide)  
    divide1(2,4)  
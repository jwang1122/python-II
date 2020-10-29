def add(x):  
    return x+1  
def sub(x):  
    return x-1  
def operator(func, x):  
    temp = func(x)  
    return temp  
print(operator(sub,10))  
print(operator(add,20))  
import functools

def add(x,y):
    return x+y

x =functools.reduce(add, range(1,101))
print(x)

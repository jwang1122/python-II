"""
Usage of passing function to another function

in this example: 
pass circle_area() function to area() function
or pass square_area() function to area() function
"""
def circle_area(r):
    return r**2*3.1416

def square_area(s):
    return s*s

def area(f, r):
    return f(r)

"""
传递功能块的妙处。
call area and pass different function, will get different result.
"""
print("14:",area(circle_area, 4))
print("15:",area(square_area, 4))

print("17:",circle_area(4))

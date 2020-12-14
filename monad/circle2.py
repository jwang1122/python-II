from math import pi
"""
raise Exception when input data type or value is wrong. 
"""
def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a real number.")
    if r < 0:
        raise ValueError("The radius cannot be negative.")    
    return pi * (r**2)

if __name__ == '__main__':
    a = circle_area(1)
    print("area=",a)
    a = circle_area(-3)
    print("area=",a)
    a = circle_area(3+4j)
    print("area=",a)
    print("Done.")
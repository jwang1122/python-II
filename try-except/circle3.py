from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError(f"The radius must be a real number, r={r}")
    if r <0:
        raise ValueError(f"the radius cannot be neigative. r={r}")
    return pi * (r**2)

try:
    area = circle_area(4)
    print("12:",area)
    area = circle_area(4.3)
    print("14:",area)
except Exception as error:
    print("12:",error)

try:
    area = circle_area(4+3j)
    print("13:",area)
except Exception as error:
    print("18:",error)

try:
    area = circle_area(-2)
    print("22:",area)
except Exception as error:
    print("24:",error)

try:
    area = circle_area("hello")
    print("22:",area)
except Exception as error:
    print("32:",error)
       
print("Done.")
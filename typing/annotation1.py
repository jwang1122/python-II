from math import pi

def circle_area(radius:float) -> float:
    return pi * radius * radius


a = circle_area(2)
print(a)

a = circle_area(True)
print(a)

a = circle_area("hello")
print(a)
from circle1 import *

def area(r):
    try:
        area = circle_area(r)
        print(f"the area with radius {r} is {area}.")
    except Exception as err:
        print("Error:", err)

area(5)
area(-5)
area(4+3j)

print("Done.")
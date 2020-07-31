from circle1 import *

r = 5
a = circle_area(r)
print("The circle area with radius %5.2f is %5.2f" %(r ,a))

r = -5
a = circle_area(r)
print("The circle area with radius %5.2f is %5.2f" %(r ,a))

r = 5 + 4j
a = circle_area(r)
print("The circle area is", a)

area = circle_area('hello')
print("17:",area)

area = circle_area(None) 
print("27:",area)

print("Done.")
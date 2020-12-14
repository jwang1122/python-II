from circle2 import circle_area

def printCircleArea(radius):
    try:
        a = circle_area(radius)
        print("The circle area with radius %6.3f is %6.3f." %(radius, a))
    except Exception as e:
        print("Error:",e)

printCircleArea(5)
printCircleArea(-5)
printCircleArea(-5+3j)
printCircleArea("hello world")

print("Done.")

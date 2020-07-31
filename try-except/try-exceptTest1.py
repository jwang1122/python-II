from circle1 import circle_area

def printCircleArea(r):
    try:
        area = circle_area(r)
        print("The circle area with radius=%5.2f is area=%5.2f" %(r,area))
    except Exception as err:
        print("Error: ", err)

if __name__ == '__main__':
    printCircleArea(1)
    printCircleArea(2.3)
    printCircleArea(-2)
    printCircleArea(-2+3j)
    printCircleArea("Hello")
    printCircleArea(None)

    print("Done.")


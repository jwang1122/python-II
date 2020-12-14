from math import pi

def circle_area(radius: float) -> float:
    """
    Calculate circle area with given radius.

    circle_area(radius,/)

    return the circle area by given radius.

    Usage:
    a = circle_area(1.0)
    print(a)

    Output:
    3.141592653589793
    """
    return pi * radius * radius


if __name__ == "__main__":
    print("Annotations:",circle_area.__annotations__)
    print(circle_area.__doc__)
    a = circle_area(1)
    print(a)
    a = circle_area(1.2+3.4j)
    print(a)
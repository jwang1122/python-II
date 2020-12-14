from math import pi


def circle_area(radius):
    return pi * radius * radius


circle_area.__doc__ = """ Calculate circle area with given radius.

The circle_area function does NOT check given radius data type.
In other word, it will calculate area for negative radius such as
circle_area(-5), complex number circle_area(3+4j).

    Usage:
        a = circle_area(1.0)

Args:
    radius: expect to be integer number, float number.

Returns:
    return area by given radius.
"""
if __name__ == "__main__":
    import     
    a = circle_area(1)
    print("area=", a)
    a = circle_area(-3)
    print("area=", a)
    a = circle_area(3 + 4j)
    print("area=", a)
    print("Done.")
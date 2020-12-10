from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError(f"The radius must be a real number, but r={r}")
    if r < 0:
        raise ValueError(f"The radius cannot be neigative, but r={r}.")    
    return pi * (r**2)
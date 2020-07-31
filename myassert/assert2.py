from math import pi

def circleArea(r):
    assert r in [int,float] and r>0, "Circle radius must be positive real number."
    return r * r * pi

a = circleArea(1.0)
print(a)

a = circleArea(-2.0)
print(a)

print("Done.")
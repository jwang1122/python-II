from math import pi


def circle_area(r):
    return r * r * pi


area = lambda r: r**2 * pi  # anonymous function, lambda expression

print(lambda r: r**2 * pi(1))
print(circle_area(1))
print(area(-2))

a = lambda r: circle_area(r)
print(a(1))
print(a(-2))

x = lambda y: y * y  # x is a function name

for i in range(5):
    print(x(i))

def foo (f, x):
    return f(x)

for i in range(5):
    print(foo(lambda x: x * x, i))

for i in range(5):
    print(foo(lambda x: x * x * x, i))

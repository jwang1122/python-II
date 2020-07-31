def f1(x):
    return 3*x + 2

def f2(x):
    return 4*x*x + 6*x + 9

def ff(f, x):
    return f(x)

# y = f1(5)
# print(y)

v = ff(f1, 7)
print(v)

v = ff(f2, 7)
print(v)
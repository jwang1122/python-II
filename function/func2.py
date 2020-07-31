"""
返回功能块的妙用。
"""
# def quadratic(a, b, c):
#     return lambda x: a*x**2 + b*x + c

def quadratic(a, b, c):
    def f(x):
        return a*x**2 + b*x + c
    return f

f = quadratic(3, 2, 5)
print("13:", type(f))
print("14:", f(4))

f2 = quadratic(2, 6, 1)
print("17:", f2(4))


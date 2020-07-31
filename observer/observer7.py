from rx import Observable,of
import operator

a = of(1, 2, 3, 4)
b = of(2, 2, 4, 4)

x = list(map(lambda a, b: operator.mul(a, b), a, b))
y = zip(b, x)
z = zip( a, y)
print(z)

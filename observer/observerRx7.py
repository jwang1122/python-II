import rx
from rx import operators as ops
import operator

a = rx.of(1, 2, 3, 4)
b = rx.of(2, 2, 4, 4)

a.pipe(
    ops.zip(b), # returns a tuple with the items of a and b
    ops.map(lambda z: operator.mul(z[0], z[1]))
).subscribe(print)

# normal way to do the same thing
a = (1, 2, 3, 4)
b = (2, 2, 4, 4)
x = list(zip(a, b))
#print(x)

y = list(map(lambda i: i[0]*i[1], x))
for i in y:
    print(i)

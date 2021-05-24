import rx
from rx import operators as ops
import operator

a = rx.of(1, 2, 3, 4)
b = rx.of(2, 2, 4, 4)

a.pipe(
    ops.zip(b),
    ops.starmap(operator.mul)
).subscribe(print)
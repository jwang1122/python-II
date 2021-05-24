from rx import Observable, from_, of, operators as op

from_(("Alpha", "Beta", "Gamma", "Delta", "Epsilon")).pipe(
    op.map(lambda s: len(s)),
    op.filter(lambda i: i >= 5)
).subscribe(lambda value: print("Received {0}".format(value)))

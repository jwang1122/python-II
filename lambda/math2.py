from pymonad.operators.maybe import Just, Nothing
from rx import Observable, of


def add3(x):
    return Just(x + 3)


def sub5(x):
    return Just(x - 5)


def mul7(x):
    return Just(x * 7)


def div9(x):
    return Just(x / 9)


f = lambda x: Just(x) >> add3 >> sub5 >> mul7 >> div9

values = of(10, 20, 30, 40, 50)
values.subscribe(
    on_next=lambda x: print(f(x)),
    on_error=lambda e: print("Error Occurred: {0}".format(e)),
    on_completed=lambda: print("Done!"),
)

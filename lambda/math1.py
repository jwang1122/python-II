from pymonad.operators.maybe import Just, Nothing

def add3(x):
    return Just(x + 3)

def sub5(x):
    return Just(x - 5)

def mul7(x):
    return Just(x * 7)

def div9(x):
    return Just(x / 9)

f = lambda x: Just(x) >> add3 >> sub5 >> mul7 >> div9

print(f(20))
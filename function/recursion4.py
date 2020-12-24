"""
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, ...
Goal: Write function to return nth term of Fibonacci Sequence.
"""
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int or n<0:
        raise TypeError("n must be a positive integer!")
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    for i in range(1, 11):
        print(f"{i}: {fibonacci(i)}")

    print(f"{i}: {fibonacci(-5)}")
except Exception as ex:
    import inspect
    cf = inspect.currentframe()
    print(f"{inspect.getframeinfo(cf).lineno}: {ex}")
print("Done.")

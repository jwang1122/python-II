"""
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, ...
Goal: Write function to return nth term of Fibonacci Sequence.
"""
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 501):
    print(f"{i}: {fibonacci(i)}")


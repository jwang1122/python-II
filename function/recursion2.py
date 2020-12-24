"""
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, ...
Goal: Write function to return nth term of Fibonacci Sequence.

very slow
"""
fibonacci_cache = {}


def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1 or n == 2:
        value = 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci_cache[n] = value
    return value


for i in range(1, 101):
    print(f"{i}: {fibonacci(i)}")

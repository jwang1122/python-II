def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

if __name__ == "__main__":
    fib(100)
    import sys
    print(sys.path)
    # fib(int(sys.argv[1]))

"""
python fib.py 100
"""
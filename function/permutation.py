from math import factorial

def fact(n):
    f = 1
    j = 1
    while(j<=n):
        f *= j
        j += 1
    return f

if __name__ == '__main__':
    l = [12, 13, 1, 6, 9]
    r = 3

    n = len(l)
    result = fact(n) / fact(n-r)
    print(f"The permutaion value for the numbers list is : {result}.")

    result = factorial(n) / factorial(n-r)
    print(f"The permutaion value for the numbers list is : {result}.")

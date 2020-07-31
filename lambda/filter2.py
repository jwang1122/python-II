import math
import os

print(os.sys.argv)

def isPrime(n): 
    if n == 2: 
        return True
    if n <= 1 or n % 2 == 0: 
        return False
    # x = list(filter(lambda i: n%i==0, range(3, 1 + math.floor(math.sqrt(n)), 2)))
    # print(n,": ",x)
    return len(list(filter(lambda i: n%i==0, range(3, 1 + math.floor(math.sqrt(n)), 2))))==0
    # for i in l: 
    #     if n % i == 0: 
    #         return False
    # return True

p = list(filter(lambda x: isPrime(x), range(500)))
print(p)
print(len(p))


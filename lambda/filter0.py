"""
filter(Function, Squence)
"""
def isEven(n):
    return n % 2 == 0

l = []
for i in range(1,11):
    if isEven(i):
        l.append(i)    
print("11:",l)

l = [e for e in range(1,11) if e%2==0]
print("14:",l)

a = range(1, 11)

print("18:",list(filter(isEven, a))) # function with name
print("19:",list(filter(lambda n: n%2==0, a))) #anonymous function
print("20:",list(filter(lambda n: n%3==0, a))) #anonymous function

def f(x):
    return x%2!=0 and x%3!=0
print("24:",list(filter(f, range(2,25))))

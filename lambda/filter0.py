def isEven(n):
    return n % 2 == 0

l = []
for i in range(1,11):
    if isEven(i):
        l.append(i)    
print("08:",l)

l = [e for e in range(1,11) if e%2==0]
print("11:",l)

a = range(1, 11)

print("15:",list(filter(isEven, a))) # function with name
print("16:",list(filter(lambda n: n%2==0, a))) #anonymous function
print("17:",list(filter(lambda n: n%3==0, a))) #anonymous function

def f(x):
    return x%2!=0 and x%3!=0
print("21:",list(filter(f, range(2,25))))

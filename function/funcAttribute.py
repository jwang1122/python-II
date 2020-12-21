""" 
function names can be attributed. 
"""
def f(x):
    f.count = getattr(f, 'count', 0) + 1 # create an attribute to function by default value 0
    return 'Returned message: Dynamically add attribute to a function'

if(__name__ == "__main__"):
    z = f("Hello")
    print(z)

    for i in range(10):
        f(i)

    print("The number of calls to the function:",f.count)

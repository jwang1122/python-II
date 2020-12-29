"""
Traditional way to handle Exception
"""
def add(x,y):
    if(type(x) not in [int, float]):
        raise TypeError(f"x must be real number. but x={x}")
        return
    return x + y


def printAddResult(x ,y):
    try:
        add(x,y)
    except Exception as err:
        print("Error: ", err)

x = add(3,6)
print("15: ",x)


printAddResult("hello", 6)

x = add(6,6)
print("21: ",x)

print("Done.")
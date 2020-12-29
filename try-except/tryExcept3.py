"""
raise Error Exception
"""
def factorial(number):
    if type(number) is not int:
        raise TypeError("The input number must to be an integer.")
    if number < 0:
        raise ValueError("The input number must to be a positive integer.") 
    f = 1
    for i in range(2, number + 1):
        f *= i
    print(f"factorial({number}) = {f}")

try:
    factorial(4)
    factorial(6)
    factorial(-4)
    factorial(5.6) # this line will not be executed
except Exception as e:
    print(e)
else:
    print("else...")
finally:
    print("finally...")

print("Done.")
def factorial(number):
    f = 1
    for i in range(2, number + 1):
        f *= i
    print(f"factorial({number}) = {f}")

try:
    factorial(4)
    factorial(6)
    factorial(-4)
#    factorial(5.6)
except Exception as e:
    print(e)
else:
    print("else...")
finally:
    print("finally...")

print("Done.")
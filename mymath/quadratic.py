import matplotlib.pyplot as plt
import numpy as np

a = 1
b = 5
c = 2

d = b*b-4.0* a*c
if d > 0.0:
    r1 = (-b + pow(d, 0.5))/(2.0*a)
    r2 = (-b - pow(d, 0.5))/(2.0*a)
    print(f"The roots are {r1} and {r2}.")
elif d==0.0:
    r = -b/(2.0 * a)
    print(f"The root is {r}.")
else:
    print("Roots are not real.")

x = np.arange(-7, 5, 0.1)
y = x * 0
plt.plot(x, a*x*x+b*x+c, 'r', label='quadratic')
plt.plot(x, y, 'b', label='root')
plt.legend(loc=2)
plt.show()
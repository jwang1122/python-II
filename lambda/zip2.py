v1 = (10, 20, 30)
v2 = (7, 5, 3)
l = list(zip(v1, v2))
print(l)
z = sum(x * y for x, y in zip(v1, v2))  # dot product
print(z)
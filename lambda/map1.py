# map lambda function to each city-temperature data
temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26),("Tokyo", 27),("New York", 28),("London", 22),("Beijing", 32)]

list1=[]
for data in temps:
    city = data[0]
    temperatur=round(9/5*data[1] + 32, 2)
    list1.append((city,temperatur))
print("09:",list1)

x = map(lambda data: (data[0], round((9 / 5) * data[1] + 32, 2)), temps)

print("13:", type(x))
y = next(x)  # get first item
print("15", y)
print("16:", list(x)) # first item has gone
print("17:", tuple(x)) # cannot print same map object second time!!! 

# solution:
x = tuple(map(lambda data: (data[0], round((9 / 5) * data[1] + 32, 2)), temps))
print("20:",x)
print("21:",x)

l = [1,2,3,4,5]
print(l)
print(l)
# map lambda function to each city-temperature data
temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26),("Tokyo", 27),("New York", 28),("London", 22),("Beijing", 32)]

list1=[]
for data in temps:
    city = data[0]
    temperatur=round(9/5*data[1] + 32, 2)
    list1.append((city,temperatur))
print("32:",list1)

x = map(lambda data: (data[0], round((9 / 5) * data[1] + 32, 2)), temps)

print("17:", type(x))
y = next(x)  # get first item
print("19", y)
print("20:", list(x))

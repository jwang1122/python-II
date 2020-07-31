def test():
    temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26), \
            ("Tokyo", 27), ("New York", 28),("London", 22),("Beijing", 32)]

    temps.sort(key=lambda data: data[0])
    print(temps)

    temps.sort(reverse=True, key=lambda data:data[1])
    print(temps)

test()
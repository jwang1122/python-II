"""
Use filter function.
"""
if(__name__ == '__main__'):
    temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26), \
            ("Tokyo", 27), ("New York", 28),("London", 22),("Beijing", 32)]
    
    x = list(filter(lambda data: data[1]>25, temps))
    print(x)

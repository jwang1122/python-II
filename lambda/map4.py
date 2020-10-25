def fahrenheit(T):
    return round((float(9) / 5) * T + 32, 2)


def celsius(T):
    return round((float(5) / 9) * (T - 32), 2)


if __name__ == "__main__":
    temp = (36.5, 37, 37.5, 39)
    f = tuple(map(fahrenheit, temp))
    c = tuple(map(celsius,f))
    print(temp)
    print(f)
    print(c)
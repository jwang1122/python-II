def test():
        name = ("Berlin", "Cairo", "Buenos Aires", "Los Angeles",
                "Tokyo", "New York", "London", "Beijing")
        temperature = (29, 36, 19, 26, 27, 28, 22, 32)

        x = list(zip(name, temperature))

        print(x)
test()
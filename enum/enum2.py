import enum

class Shake(enum.Enum): # both key and value must to be unique
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES  = 9
    MINT  = 3

if __name__ == '__main__':
    for shake in Shake:
        print(shake)
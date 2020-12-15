from enum import Enum

class Shake(Enum): # both key and value must to be unique
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES  = 9
    MINT  = 3
#    MINT  = 1
    VANILLA_ALIAS = 7

if __name__ == '__main__':
    for shake in Shake:
        print(shake)
    print()
    print(Shake.VANILLA_ALIAS)
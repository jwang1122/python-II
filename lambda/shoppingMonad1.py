from pymonad.operators.maybe import Just, Nothing
from pymonad.list import *

def writeShoppingList(x):
    return Just(f"{x} prepare shopping list.")

def driveToMarket(x):
    return Just(x + "\n> Drive to the market.")

def findThing(x):
    return Just(x + "\n> Find stuff need to buy.")

def checkout(x):
    return Just(x + "\n> Check out, pay credit card.")

def driveBackHome(x):
    return Just(x + "\n> Drive home.")

x= Just("John ") >> writeShoppingList >> driveToMarket >> checkout >> driveBackHome
print("20:",x)

list1 = ListMonad(writeShoppingList, driveToMarket,findThing,checkout,driveBackHome)
x = Just("Wei")
for f in list1:
    x = x >> f

print("27:",x)

print("Done.")
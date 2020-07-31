from pymonad import *

def writeShoppingList(x):
    return Just("\n" + x+" prepare shopping list.")

def driveToMarket(x):
    return Just(x+"\nDrive to the market.")

def findThing(x):
    return Just(x + "\nFind stuff need to buy.")

def checkout(x):
    return Just(x + "\nCheck out, pay credit card.")

def driveBackHome(x):
    return Just(x + "\nDrive home.")

x= Just("John ") >> writeShoppingList >> driveToMarket >> checkout >> driveBackHome
print("11:",x)

list1 = List(writeShoppingList, driveToMarket,findThing,checkout,driveBackHome)
x = Just("Wei")
for f in list1:
    x = x >> f

print(x)

persons = List("John", "Wei", "Jun")

# x = persons >> list1
# print(x)
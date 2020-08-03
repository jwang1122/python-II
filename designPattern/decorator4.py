class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.items = []

    def __repr__(self):
        return "%20s\t$%5.2f" % (self.name, self.price)

class Decorator:
    name = ""
    price = 0.0
    def __init__(self, item):
        myitem = Item(self.name, self.price)
        self.price = item.price + myitem.price
        self.items = item.items
        self.items.append(myitem)

    def __repr__(self):
        result = ""
        for item in self.items:
            result += f"\n{item}"
        return result + "\n%20s\t$%5.2f" % ("total:",self.price)

class BaseBurger:
    def __init__(self):
        item = Item("Burger Base", 1.0)
        self.price = item.price
        self.items =[item,]

class Cheese(Decorator):
    name = "Cheese"
    price = 0.5

class Fries(Decorator):
    name = "Franch Fries"
    price = 2.5

class LargeDrinks(Decorator):
    name = "Large Drinks"
    price = 1.5

order = Cheese(BaseBurger())
print(order)

order = Fries(Cheese(BaseBurger()))
print(order)

order = LargeDrinks(Fries(Cheese(BaseBurger())))
print(order)

order = LargeDrinks(Fries(BaseBurger()))
print(order)
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        items = []

    def addItem(self, item):
        items.append(item)
    
    def totalPrice(self):
        total = 0.0
        for item in items:
            total += item.price
        return total
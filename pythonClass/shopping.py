class item:
    
    def __init__(self, name, price:float):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name

class lineItem:
    def __init__(self, product=None, quantity=0):
        self.item = product
        self.quantity = quantity
        self.subtotal = product.price * quantity

    def __repr__(self):
        return self.item.name + ": \t" + str(self.subtotal)

class order:
    def __init__(self):
        self.items = []

    def addLineItem(self, lineItem):
        self.items.append(lineItem)

    def printOrder(self):
        total = 0
        for i in self.items:
            print(i)
            total += i.subtotal
        print("Total: $%5.2f" %total)
        
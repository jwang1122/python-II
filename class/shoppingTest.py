from shopping import *

myOrder = order() 

banana=item("banana",3.59)
bananas = lineItem(banana, 3)
myOrder.addLineItem(bananas)

apple = item("apple",1.99)
apples = lineItem(apple, 5)
myOrder.addLineItem(apples)

myOrder.printOrder()

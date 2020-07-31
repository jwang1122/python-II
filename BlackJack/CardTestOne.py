from card import *

c1 = Card(4, "DIAMOND")
c2 = Card(4, "HEART")

print(c1 == c2)

c1 = Card(1, "CLUB")
print(c1.getValue())

c1 = BlackJackCard(1, "CLUB")
print(c1.getValue())

c1 = BlackJackCard(13, "CLUB")
print(c1.getValue())

c1 = BlackJackCard(9, "CLUB")
print(c1.getValue())

c1 = BlackJackCard(0, "CLUB")
print(c1.getValue())
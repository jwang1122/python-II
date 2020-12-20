from card0 import *

deck = Deck()

for i in range(Deck.NUMCARDS):
    c = deck.nextCard()
    print(i, ":", c, c.getValue())
print()

deck.shuffle()

for j in range(Deck.NUMCARDS):
    print(j, ":", deck.nextCard())
print()

from card import *

p1 = Player()
deck = Deck()
deck.shuffle()

p1.addCardToHand(deck.nextCard())
p1.addCardToHand(deck.nextCard())

print(p1)
print("hand value:")
print(p1.getHandValue())

p1.addCardToHand(deck.nextCard())
p1.addCardToHand(deck.nextCard())

print(p1)
print("hand value:")
print(p1.getHandValue())

print(p1.hit())
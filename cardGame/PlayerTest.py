from card import *

p1 = Player("John")
deck = Deck()
deck.shuffle()

p1.addCardToHand(deck.nextCard())
p1.addCardToHand(deck.nextCard())

print(p1)
print("hand value:")
print(p1.getHandValue())
hit = p1.hit()
while hit:
    p1.addCardToHand(deck.nextCard())

    print(p1)
    print("hand value:")
    print(p1.getHandValue())
    hit = p1.hit()

print("Done")
from card0 import *

dealer = Dealer()
player = Player("John")

dealer.shuffle()
    
player.addCardToHand(dealer.deal())
dealer.addCardToHand(dealer.deal())
player.addCardToHand(dealer.deal())
dealer.addCardToHand(dealer.deal())

playerTotal = player.getHandValue()
dealerTotal = dealer.getHandValue()

print("Player:")
print("Hand Value:: ", playerTotal)
print("Hand Size:: ", player.getHandSize())
print("Cards in Hand:: ", player)

print("Dealer:")
print("Hand Value:: ", dealerTotal)
print("Hand Size:: ", dealer.getHandSize())
print("Cards in Hand:: ", dealer)

if playerTotal>21 and dealerTotal<=21:
    print("Dealer wins - Player busted!")
elif playerTotal<=21 and dealerTotal>21:
    print("Player wins - Dealer busted!")
elif playerTotal>21 and dealerTotal>21:
    print("Both players bust!")
elif playerTotal<dealerTotal:
    print("Dealer has bigger hand value!")
else:
    print("Player has bigger hand value!")


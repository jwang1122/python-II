import random
from abc import ABC, abstractmethod 

class Card(ABC):
    # constructor
    def __init__(self, face, suit):
        # instance variables
        self.face = face
        self.suit = suit

    def __repr__(self):
        return " of ".join((Deck.FACES[self.face], self.suit))

    # @abstractmethod  
    def getValue(self):
        return self.face + 1

    def __eq__(self, other):
        return self.getValue() == other.getValue()

    # def __gt__(self, other):
        return self.getValue() > other.getValue()

    def __lt__(self, other):
        return self.getValue() > other.getValue()

    def __add__(self, other):
        return self.getValue() + other.getValue()
        
class BlackJackCard(Card):
    def getValue(self):
        if (self.face == 0):
            return 11
        elif (self.face > 8):
            return 10
        return self.face + 1


class Deck:
    FACES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ('Diamonds', "Clubs", "Spades", "Hearts")
    NUMFACES = 13
    NUMSUITS = 4
    NUMCARDS = 52

    def __init__(self):
        # initialize data - stackOfCards - topCardIndex
        self.topCardIndex = 51
        self.stackOfCards = [BlackJackCard(f, s) for s in Deck.SUITS for f in range(len(Deck.FACES))]

    def __len__(self):
        return self.topCardIndex

    def setTopCardIndex(self, n):
        self.topCardIndex = n

    def shuffle(self):
        random.shuffle(self.stackOfCards)
        self.topCardIndex = 51

    def getCard(self):
        return self.topCardIndex

    def size(self):
        return 52

    def numCardsLeft(self):
        return self.topCardIndex

    def nextCard(self):
        self.topCardIndex -= 1
        return self.stackOfCards[self.topCardIndex]


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.win = 0

    def __repr__(self):
        return self.name + ": " + str(self.hand) + ": " + str(self.getHandValue()) + ": win " + str(self.win)

    def addCardToHand(self, card):
        self.hand.append(card)

    def increaseWin(self):
        self.win += 1

    def cleanHand(self):
        self.hand = []

    def getHandValue(self):
        a = 0
        hasA = False
        for c in self.hand:
            if (c.face == 0):
                hasA = True
            a += c.getValue()
        if a > 21 and hasA:
            a -= 10
        return a

    def getHandSize(self):
        return len(self.hand)

    def hit(self):
        value = self.getHandValue()
        if value >= 20:
            return False
        if value <= 10:
            return True
        answer = input("Do you want to hit? (y or n): ")
        return True if answer == 'y' else False

class Dealer(Player):
    def __init__(self):
        self.deck = Deck()
        self.hand = []
        self.name = "Dealer"
        self.win = 0
        
    def shuffle(self):
        self.deck.shuffle()
    
    def deal(self):
        return self.deck.nextCard()

    def hit(self):
        value = self.getHandValue()
        if value < 17:
            return True
        return False
    
def playGame():
    dealer = Dealer()
    player = Player("John")
    gameOver = False
    while gameOver == False:
        dealer.shuffle()
        player.cleanHand()
        dealer.cleanHand()
        player.addCardToHand(dealer.deal())
        dealer.addCardToHand(dealer.deal())
        player.addCardToHand(dealer.deal())
        dealer.addCardToHand(dealer.deal())
        print(player)
        print(dealer)
        hit = player.hit()
        while hit:
            player.addCardToHand(dealer.deal())
            if dealer.hit():
                dealer.addCardToHand(dealer.deal())
            print(player)
            print(dealer)
            hit = player.hit()
        while dealer.hit():
            dealer.addCardToHand(dealer.deal())
        playerTotal = player.getHandValue()
        dealerTotal = dealer.getHandValue()

        if playerTotal>21 and dealerTotal<=21:
            dealer.increaseWin()
            print("Dealer wins - Player busted!")
        elif playerTotal<=21 and dealerTotal>21:
            player.increaseWin()
            print("Player wins - Dealer busted!")
        elif playerTotal>21 and dealerTotal>21:
            print("Both players bust!")
        elif playerTotal<dealerTotal:
            dealer.increaseWin()
            print("Dealer has bigger hand value!")
        else:
            player.increaseWin()
            print("Player has bigger hand value!")
        print(player)
        print(dealer)

        answer = input("Do you want to play again? (y or n) ").lower()
        if answer != 'y':
            gameOver = True
        
if __name__ == '__main__':
    # playGame()
    # try:
    #     c1 = Card(12,"Hearts")
    #     print(c1)
    # except Exception as err:
    #     print(err)
    # b1 = BlackJackCard(12,"Clubs")
    # print(b1)
    # deck1 = Deck()
    # print(len(deck1))
    # deck1.nextCard()
    # print(len(deck1))
    c1 = Card(12,"Hearts")
    c2 = Card(10,"Clubs")
    d = c1.__add__(c2)
    print(d)
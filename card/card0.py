"""
Single Player vs Dealer Black Jack Card Game
"""
import random
from abc import ABC, abstractmethod 
from typing import List

class Card(ABC):
    # constructor
    def __init__(self, face, suit):
        # instance variables
        self.face = face
        self.suit = suit

    def __repr__(self):
        return " of ".join((self.face, self.suit))

     
    # @abstractmethod  
    def getValue(self):
        switch = {"A":1,"J":11,"Q":12,"K":13}
        if self.face.isdigit():
            return int(self.face)
        return switch.get(self.face)

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
        switch = {"A":11,"J":10,"Q":10,"K":10}
        if self.face.isdigit():
            return int(self.face)
        return switch.get(self.face)


class Deck:
    FACES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ('Diamonds', "Clubs", "Spades", "Hearts")
    NUMFACES = 13
    NUMSUITS = 4
    NUMCARDS = 52

    def __init__(self):
        # initialize data - stackOfCards - topCardIndex
        self.topCardIndex = 52
        self.stackOfCards = [BlackJackCard(f, s) for s in Deck.SUITS for f in Deck.FACES]

    def __len__(self):
        return self.topCardIndex

    def setTopCardIndex(self, n):
        self.topCardIndex = n

    def shuffle(self):
        random.shuffle(self.stackOfCards)
        self.topCardIndex = 52

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
            if (c.face == "A"):
                hasA = True
            a += c.getValue()
            if(a>21 and hasA):
                a -= 10
                hasA = False
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

    def showHand(self):
        print(self.__repr__())

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
    
    def showHand(self):
        print(self.name, end=': ')
        print("[", end='')
        count = 1
        for c in self.hand:
            if count != len(self.hand):
                print(c, end=', ')
            else:
                print("Hiden]")
            count += 1

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
        dealer.showHand()
        hit = player.hit()
        while hit:
            player.addCardToHand(dealer.deal())
            if dealer.hit():
                dealer.addCardToHand(dealer.deal())
            print(player)
            dealer.showHand()
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
        elif playerTotal == dealerTotal :
            print("The player and dealer have same hand value.")
        else:
            player.increaseWin()
            print("Player has bigger hand value!")
        print(player)
        print(dealer)

        answer = input("Do you want to play again? (y or n) ").lower()
        if answer != 'y':
            gameOver = True
        
if __name__ == '__main__':
    playGame()
    # deck1 = Deck()
    # print(len(deck1))
    # deck1.nextCard()
    # print(len(deck1))
    # c1 = BlackJackCard("J","Hearts")
    # c2 = BlackJackCard("A","Clubs")
    # d = c1+c2
    # print(d)
    # c1 = BlackJackCard("2","Hearts")
    # c2 = BlackJackCard("5","Clubs")
    # c3 = BlackJackCard("A","Diamonds")

    # dealer = Dealer()
    # dealer.addCardToHand(c1)
    # dealer.addCardToHand(c2)
    # dealer.addCardToHand(c3)
    # dealer.showHand()
    
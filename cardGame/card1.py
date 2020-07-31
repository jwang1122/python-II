"""
Multi-Players vs Dealer Black Jack Card Game
"""
import random

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return " of ".join((self.face, self.suit))

    def __lt__(self, other):
        return self.getValue() < other.getValue()
    def __gt__(self, other):
        return self.getValue() > other.getValue()
    def __eq__(self, other):
        return self.getValue() == other.getValue()
    
    def getValue(self):
        d1 = {"A":1, "J":11, "Q":12, "K":13}
        if self.face.isdigit():
            return int(self.face)
        return d1.get(self.face)

class BlackJackCard(Card):
    def getValue(self):
        d1 = {"A":11, "J":10, "Q":10, "K":10}
        if self.face.isdigit():
            return int(self.face)
        return d1.get(self.face)

class Deck:
    FACES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ('Diamonds', "Clubs", "Spades", "Hearts")
    NUMFACES = 13
    NUMSUITS = 4
    NUMCARDS = 52

    def __init__(self):
        # initialize data - stackOfCards - topCardIndex
        self.topCardIndex = 52
        # self.stackOfCards = [BlackJackCard(f, s) for s in Deck.SUITS for f in Deck.FACES]
        self.stackOfCards = []
        for f in Deck.FACES:
            for s in Deck.SUITS:
                bj = BlackJackCard(f, s)
                self.stackOfCards.append(bj)

    def nextCard(self):
        self.topCardIndex -= 1
        return self.stackOfCards[self.topCardIndex]

    def shuffle(self):
        random.shuffle(self.stackOfCards)
        self.topCardIndex = 52

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.win = 0
    
    def __repr__(self):
        return self.name + ": " + str(self.hand) + ": " + str(self.getHandValue()) + ": win " + str(self.win)

    def addCardToHand(self, card):
        self.hand.append(card)

    def getHandValue(self):
        total = 0
        hasA = False
        for c in self.hand:
            if c.face == "A":
                hasA = True
            total += c.getValue()
            if total > 21 and hasA:
                total -= 10
                hasA = False
        return total

    def hit(self):
        value = self.getHandValue()
        if value >= 20:
            return False
        elif value <= 10:
            return True
        answer = input(f"{self.name}: Do you want to hit? (y/n) ")
        return True if answer == 'y' else False

    def cleanHand(self):
        self.hand = []

    def increaseWin(self):
        self.win += 1

    def showHand(self):
        return self.name + ": " + str(self.hand) + ": " + str(self.getHandValue())

    def getHandSize(self):
        return len(self.hand)

class Dealer(Player):
    def __init__(self):
        self.deck = Deck()
        self.name = "Dealer"
        self.hand = []
        self.win = 0

    def hit(self):
        value = self.getHandValue()
        if value < 17:
            return True
        return False

    def deal(self):
        return self.deck.nextCard()

    def showHand(self):
        output = self.name + "["
        count = 1
        for c in self.hand:
            if count != len(self.hand):
                output += str(c) + ", "
            else:
                output += "Hidden]"
            count += 1
        return output

    def shuffle(self):
        self.deck.shuffle()

class Game:
    def __init__(self):
        self.players = []
        self.dealer = Dealer()

    def addPlayer(self, player):
        self.players.append(player)

    def addAllPlayers(self):
        morePlayer = True
        while morePlayer:
            name = input("please enter player's name: ")
            player = Player(name)
            self.addPlayer(player)
            answer = input("More player? (y/n) ")
            if answer != "y":
                morePlayer = False

    def cleanAllPlayersHand(self):
        for player in self.players:
            player.cleanHand()

    def dealCardToAllPlayers(self):
        for player in self.players:
            player.addCardToHand(self.dealer.deal())

    def showAllPlayersHand(self):
       for player in self.players:
           print(player.showHand())

    def determineWinner(self):
        dealerTotal = self.dealer.getHandValue()
        for player in self.players:
            playerTotal = player.getHandValue()

            if playerTotal>21 and dealerTotal<=21:
                self.dealer.increaseWin()
            elif playerTotal<=21 and dealerTotal>21:
                player.increaseWin()
            elif playerTotal>21 and dealerTotal>21:
                pass
            elif playerTotal<dealerTotal:
                self.dealer.increaseWin()
            elif playerTotal == dealerTotal:
                pass
            else:
                player.increaseWin()

    def showResult(self):
        for player in self.players:
            print(player)
        print(self.dealer)

    def play(self):
        self.addAllPlayers()
        gameOver = False
        while not gameOver:
            self.dealer.shuffle()
            self.cleanAllPlayersHand()
            self.dealer.cleanHand()
            
            self.dealCardToAllPlayers()
            self.dealer.addCardToHand(self.dealer.deal())
            self.dealCardToAllPlayers()
            self.dealer.addCardToHand(self.dealer.deal())
            self.showAllPlayersHand()
            print(self.dealer.showHand())
            for player in self.players:
                hit = player.hit()
                while hit:
                    player.addCardToHand(self.dealer.deal())
                    print(player.showHand())
                    hit = player.hit()
            while self.dealer.hit():
                self.dealer.addCardToHand(self.dealer.deal())
            self.determineWinner()
            self.showResult()
 
            answer = input("Do you want to play again? (y or n) ").lower()
            if answer != 'y':
                gameOver = True


if __name__ == '__main__':
    game = Game()
    game.play()

    # game.addAllPlayers()
    # print(game.players)

    # c1 = Card("A", "Clubs")
    # print(c1)
    # print(c1.getValue())
    # c1 = Card("10", "Hearts")
    # print(c1)

    # b1 = BlackJackCard("A","Spades")
    # print(b1)
    # print(b1.getValue())    
    # b1 = BlackJackCard("J","Spades")
    # print(b1)
    # print(b1.getValue())

    # john = Player("John")
    # b1 = BlackJackCard("2","Spades")
    # b2 = BlackJackCard("J","Hearts")
    # b3 = BlackJackCard("4","Clubs")
    # john.addCardToHand(b1)
    # john.addCardToHand(b2)
    # john.addCardToHand(b3)
    # print(john.showHand())

    # dealer = Dealer()
    # b1 = BlackJackCard("2","Spades")
    # b2 = BlackJackCard("J","Hearts")
    # b3 = BlackJackCard("4","Clubs")
    # dealer.addCardToHand(b1)
    # dealer.addCardToHand(b2)
    # dealer.addCardToHand(b3)
    # print(dealer.showHand())

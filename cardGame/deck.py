
class Deck:
    NUMFACES = 13
    NUMSUITS = 4
    NUMCARDS = 52

    FACES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    SUITS = ('Spades','Clubs','Hearts','Diamonds')

    def __init__(self):
        # initialize data - stackOfCards - topCardIndex
        self.topCardIndex = 51
       self.stackOfCards = [BlackJackCard(f, s) for s in Deck.SUITS for f in range(len(Deck.FACES))]

        # loop through suits
		# loop through faces
		# add in a new card

    def __repr__(self):
        return 

    def __len__(self):
        return self.topCardIndex

    def setTopCardIndex(self, n):
        # setter
        pass

    def setStackOfCards(self,cards):
        # setter
        pass

    def shuffle(self):
        # shuffle the deck
        # reset variables as needed
        pass

    def getCard(self):
        return self.topCardIndex

    def size(self):
        return 52

    def numCardsLeft(self):
        return 0

    def nextCard(self):
        self.topCardIndex -= 1
        return self.stackOfCards[self.topCardIndex]

if __name__ == '__main__':
    d1 = Deck()
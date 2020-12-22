from enum import Enum
from pprint import pprint
import abc


class Suits(Enum):
    SPADES = 1
    CLUBS = 2
    DIAMONDS = 3
    HEARTS = 4


class Faces(Enum):  # the value must to be unique
    ACE = "A"
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = "J"
    QUEEN = "Q"
    KING = "K"


class Card(abc.ABC):
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face.value}, {self.suit.name})"

    def __eq__(self, other):
        return self.getValue() == other.getValue()

    def __lt__(self, other):
        return self.getValue() < other.getValue()
        
    def __gt__(self, other):
        return self.getValue() > other.getValue()
        
    def __call__(self, face, suit):
        return

    @abc.abstractmethod
    def getValue(self):
        pass


class BlackJackCard(Card):
    def getValue(self):
        switch = {Faces.JACK: 10, Faces.QUEEN: 10, Faces.KING: 10, Faces.ACE: 11}
        if self.face in (Faces.JACK, Faces.QUEEN, Faces.KING, Faces.ACE):
            return switch.get(self.face)
        return self.face.value


class Deck:
    def __init__(self):
        self.cards = [BlackJackCard(f, s) for s in Suits for f in Faces]


if __name__ == "__main__":
    for face in Faces:
        print(face)

    for suit in Suits:
        print(suit)

    deck = Deck()
    print(deck.cards)    
    print(len(deck.cards))

    diamondA = BlackJackCard(Faces.ACE, Suits.DIAMONDS)
    print(diamondA)
    print(diamondA)

#    club2 = Card(Faces.TWO, Suits.CLUBS)
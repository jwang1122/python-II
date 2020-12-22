from enum import Enum
from pprint import pprint


class Suits(Enum):
    SPADE = 1
    CLUB = 2
    DIAMOND = 3
    HEART = 4


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


class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face.value}, {self.suit.name})"

    def getValue(self):
        switch = {Faces.JACK:11, Faces.QUEEN:12, Faces.KING:13, Faces.ACE:1}
        if self.face in (Faces.JACK, Faces.QUEEN, Faces.KING, Faces.ACE):
            return switch.get(self.face)
        return self.face.value


if __name__ == "__main__":
    diamondA = Card(Faces.ACE, Suits.DIAMOND)
    print(diamondA)
    print(diamondA.getValue())
    diamondQ = Card(Faces.QUEEN, Suits.DIAMOND)
    print(diamondQ)
    print(diamondQ.getValue())
    club2 = Card(Faces.TWO, Suits.CLUB)
    print(club2)
    print(club2.getValue())

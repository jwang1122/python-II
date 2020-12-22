from enum import Enum
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

    def getValue(self):
        switch={Faces.ACE:1, Faces.JACK:11, Faces.QUEEN:12, Faces.KING:13}
        if self.face in (Faces.ACE, Faces.JACK, Faces.QUEEN, Faces.KING):
            return switch.get(self.face)
        return self.face.value

from enum import Enum
from pprint import pprint
"""
Class level function
Class level attribute
"""

class Suits(Enum):
    SPADE=1
    CLUB=2
    DIAMOND=3
    HEART=4

class Faces(Enum): # the value must to be unique
    ACE='A'
    TWO=2 
    THREE=3
    FOUR=4
    FIVE=5
    SIX=6
    SEVEN=7
    EIGHT=8
    NINE=9
    TEN=10
    JACK='J'
    QUEEN='Q'
    KING='K'

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face.value}, {self.suit.name})"
    
    def getValue(self):
        if self.face in (Faces.JACK, Faces.QUEEN, Faces.KING):
            return 10
        if self.face in (Faces.ACE,):
            return 1
        return self.face.value

class Deck:
    def __init__(self):
        self.deck = [Card(f, s) for s in Suits for f in Faces]
                
if __name__ == '__main__':
    for face in Faces:
        print(face)

    for suit in Suits:
        print(suit)
    
    print("48:",Faces['TWO'])
    member = Faces.TEN
    print(member.name)
    print(member.value)
    print(member.value + 11)

    diamond9 = Card(Faces.NINE, Suits.DIAMOND)
    print(diamond9)
    print(diamond9.getValue())

    deck = Deck()
    pprint(deck.deck)
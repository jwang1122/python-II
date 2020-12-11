from pprint import pprint

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    
    def __repr__(self):
        return f"({self.face}, {self.suit})"

faces = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["SPADE","CLUB","DIAMOND","HEART"]
squares = [x**2 for x in range(10)]
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

cards = [Card(face, suit) for face in faces for suit in suits]
pprint(cards)

cards = list(map(lambda face, suit: Card(face, suit), faces, suits))
pprint(cards) # map need two iterable have same length

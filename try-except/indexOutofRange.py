"""
IndexError: tuple index out of range
"""
class Card:
    FACES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ('Diamonds', "Clubs", "Spades", "Hearts")

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    
    def __repr__(self):
        return f"({self.face}, {self.suit})"
    

if __name__ == '__main__':
    diamondA = Card(Card.FACES[0], Card.SUITS[0])
    print(diamondA)

    card = Card(Card.FACES[13], Card.SUITS[0])
    print(card)
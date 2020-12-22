class Card:
    FACES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ('Diamonds', "Clubs", "Spades", "Hearts")

    def __init__(self, face, suit):
        self.face = str(face)
        self.suit = suit
    
    def __repr__(self):
        return f"({self.face}, {self.suit})"

    def __eq__(self, other):
        return self.getValue() == other.getValue()
        
    def getValue(self):
        switch = {"A":1,"J":11,"Q":12,"K":13}
        if self.face.isdigit():
            return int(self.face)
        return switch.get(self.face, 0)
        
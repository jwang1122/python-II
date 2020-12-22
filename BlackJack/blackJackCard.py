from card import Card

class BlackJackCard(Card):
    def getValue(self):
        if(self.face == 1):
            return 11
        elif(self.face > 9):
            return 10
        return self.face

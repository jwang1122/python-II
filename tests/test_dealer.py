import unittest
from card import *

class TestDealer(unittest.TestCase):
    def test_getHandValue(self):
        dealer = Dealer()
        ACE = BlackJackCard("A", "Diamonds")
        h7= BlackJackCard("7", "Hearts")
        c7= BlackJackCard("7", "Clubs")
        
        dealer.addCardToHand(ACE)
        dealer.addCardToHand(h7)
        dealer.addCardToHand(c7)
        self.assertEqual(dealer.getHandValue(), 15)
        self.assertEqual(dealer.hit(), True)
        c2 = BlackJackCard("2", "Clubs")
        dealer.addCardToHand(c2)
        self.assertEqual(dealer.getHandValue(), 17)
        self.assertEqual(dealer.hit(), False)

    def test_deal(self):
        dealer = Dealer()
        c = BlackJackCard("K", "Hearts")
        c1 = dealer.deal()
        self.assertEqual(c1, c)
import unittest
from card import *

class TestPlayer(unittest.TestCase):
    def test_getHandValue(self):
        john = Player("John")
        d2 = BlackJackCard("2", "Diamonds")
        h7= BlackJackCard("7", "Hearts")
        c7= BlackJackCard("7", "Clubs")
        
        john.addCardToHand(d2)
        john.addCardToHand(h7)
        john.addCardToHand(c7)
        self.assertEqual(john.getHandValue(), 16)
        
    def test_valueGreaterThan21(self):
        john = Player("John")
        dA = BlackJackCard("A", "Diamonds")
        h7= BlackJackCard("7", "Hearts")
        c7= BlackJackCard("7", "Clubs")
        
        john.addCardToHand(dA)
        john.addCardToHand(h7)
        john.addCardToHand(c7)
        self.assertEqual(john.getHandValue(), 15)

    def test_twoA(self):
        john = Player("John")
        dA = BlackJackCard("A", "Diamonds")
        hA= BlackJackCard("A", "Hearts")
        c7= BlackJackCard("2", "Clubs")
        
        john.addCardToHand(dA)
        john.addCardToHand(hA)
        john.addCardToHand(c7)
        self.assertEqual(john.getHandValue(), 14)

    def test_twoAonly(self):
        john = Player("John")
        dA = BlackJackCard("A", "Diamonds")
        hA= BlackJackCard("A", "Hearts")
        
        john.addCardToHand(dA)
        john.addCardToHand(hA)
        self.assertEqual(john.getHandValue(), 12)

    def test_threeA(self):
        john = Player("John")
        dA = BlackJackCard("A", "Diamonds")
        h2= BlackJackCard("2", "Hearts")
        hA= BlackJackCard("A", "Hearts")
        cA= BlackJackCard("A", "Clubs")
        
        john.addCardToHand(dA)
        john.addCardToHand(h2)
        john.addCardToHand(hA)
        john.addCardToHand(cA)
        self.assertEqual(john.getHandValue(), 15)

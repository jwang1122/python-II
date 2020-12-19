import unittest
from cardGame.card4 import *

class TestDeck(unittest.TestCase):
    def test_init(self):
        deck = Deck()
        self.assertEqual(len(deck.stackOfCards), 52)
    
    def test_shuffle(self):
        deck = Deck()
        c1 = deck.nextCard()
        self.assertEqual(c1.face,"K")
        self.assertEqual(c1.suit,"Hearts")
        deck.shuffle()
        c1 = deck.nextCard()
        self.assertNotEqual(c1.face,"K")

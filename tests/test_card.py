import unittest
from level2.card import *

class TestBlackJackCard(unittest.TestCase):
    def test_faces(self):
        c1 = BlackJackCard("A", "DIAMONDS")
        self.assertEqual(c1.getValue(), 11)
        c1 = BlackJackCard("8", "DIAMONDS")
        self.assertEqual(c1.getValue(), 8)
        c1 = BlackJackCard("10", "DIAMONDS")
        self.assertEqual(c1.getValue(), 10)
        c1 = BlackJackCard("Q", "DIAMONDS")
        self.assertEqual(c1.getValue(), 10)
        c1 = Card("A","Diamonds")
        c2 = Card("2", "Hearts")
        self.assertEqual(c2<c1, True)
        c1 = Card("Q","Diamonds")
        c2 = Card("J", "Hearts")
        self.assertEqual(c2<c1, False)
        self.assertEqual(c1+c2, 23)
    
    def test_EqualValue(self):
        c1 = BlackJackCard("J", "DIAMONDS")
        c2 = BlackJackCard("K", "HEARTS")
        self.assertEquals(c1.getValue(), c2.getValue())
        self.assertEqual(c1==c2, True)
 
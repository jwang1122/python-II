import unittest
from BlackJack.card2 import Card, Faces, Suits

class TestBlackJackCard(unittest.TestCase):
    def test_getValue(self):
        dimondA = Card(Faces.ACE, Suits.DIAMONDS)
        self.assertEqual(dimondA.getValue(), 1)
        club2 = Card(Faces.TWO, Suits.CLUBS)
        self.assertTrue(club2.getValue()==2)
        clubJ = Card(Faces.JACK, Suits.CLUBS)
        self.assertTrue(clubJ.getValue()==11)
        heartQ = Card(Faces.QUEEN, Suits.HEARTS)
        dimondQ = Card(Faces.QUEEN, Suits.DIAMONDS)
        self.assertTrue(clubJ < heartQ)
        self.assertTrue(club2 < heartQ)
        self.assertFalse(club2 > heartQ)
        self.assertEqual(dimondQ, heartQ)

import unittest
from cardGame.card5 import BlackJackCard, Card, Faces, Suits

class TestBlackJackCard(unittest.TestCase):
    def test_getValue(self):
        dimondA = BlackJackCard(Faces.ACE, Suits.DIAMONDS)
        self.assertEqual(dimondA.getValue(), 11)
        club2 = BlackJackCard(Faces.TWO, Suits.CLUBS)
        self.assertTrue(club2.getValue()==2)
        clubJ = BlackJackCard(Faces.JACK, Suits.CLUBS)
        self.assertTrue(clubJ.getValue()==10)
        heartQ = BlackJackCard(Faces.QUEEN, Suits.HEARTS)
        self.assertTrue(clubJ == heartQ)
        self.assertTrue(club2 < heartQ)
        self.assertFalse(club2 > heartQ)
    
    def test_invalidType(self):
        self.assertRaises(TypeError, Card, None, None) # make Card callable       
       

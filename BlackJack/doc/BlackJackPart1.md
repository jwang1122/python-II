# Black Jack Card Game - Part 1

## Involved Class

Card; BlackJackCard; 

## Involved Function
CardTestOne()

## Initial Code
* Finish the Card class below
```py
class Card:
    faces = ("ZERO", "ACE", "TWO", "THREE","FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK","QUEEN", "KING")
    suits = ('DIAMONDS', "CLUBS", "SPADES", "HEARTS")

    # constructor
    def __init__(self, face, suit):
        # instance variables    
        # your code goes her
        pass

    def __str__(self):
        return # your code goes here

    def getValue(self):
        return # your code goes here

    def __eq__(self, other):
        return # your code goes here

```
Expected output:
```py
card1 = Card(1, 'DIAMONDS')
print(card1)
```
(ACE, DIAMONDS value=1)

* Next, finish the BlackJackCard class, for right now ACES count as 11 while TEN, JACK, QUEEN, and KING count as 10.

```py
class BlackJackCard(Card):
    # constructor

    def getValue(self):
        # enables you to build the value for the game into
        # the card. This makes writing the whole program
        # a little easier.

```

* Test your classes using the CardTestOne() function

```py
def CardTestOne():
    # create some card, make sure output are correct
    # compare your existing two cards, use dunder __eq__ to see if the values are equal
    # your code here
```

* Write unittest test all possibilities, handle all possible input errors.

>>> from card import *
>>> c1 = BlackJackCard(10, "HEARTS")
>>> c2 = BlackJackCard(13, "CLUBS")
>>> print(c1 == c2)
True

>>> c1 = BlackJackCard(0, "HEARTS")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/wangqianjiang/workspace/playground/card.py", line 9, in __init__
    raise ValueError("Invalid Card Face!")  
ValueError: Invalid Card Face!

>>> c1 = BlackJackCard(5, "HEART")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/wangqianjiang/workspace/playground/card.py", line 11, in __init__
    raise ValueError("Invalid Card Suit!") 
ValueError: Invalid Card Suit!
from card import *
try:
    c1 = Card(4, "Diamonds")
    print(c1.getValue())
    c2 = Card(4, "Hearts")

    print(c1 == c2)

    c1 = Card(11, "Clubs")
    print(c1.getValue())

    c1 = BlackJackCard(11, "Clubs")
    print(c1.getValue())

    c1 = BlackJackCard(13, "Clubs")
    print(c1)
    print(c1.getValue())

    c1 = BlackJackCard(9, "Clubs")
    print(c1)
    print(c1.getValue())

    c1 = BlackJackCard(0, "Clubs")
    print(c1)
    print(c1.getValue())
except Exception as err:
    print(err)


print("Done.")
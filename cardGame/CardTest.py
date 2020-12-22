from card import Card
"""
card = Card("15", "MySuit")
easily make mistake
"""

try:
    c1 = Card("4", "Diamonds")
    print(c1.getValue())
    c2 = Card("4", "Hearts")

    print(c1 == c2)

    c1 = Card("11", "Clubs")
    print(c1.getValue())

except Exception as err:
    print(err)


print("Done.")
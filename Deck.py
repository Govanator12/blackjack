import random as r

class Deck(object):
    """This simulates the deck"""

    def __init__(self):
        self.deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4

    def resetDeck(self):
        self.deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4
        r.shuffle(self.deck)

    def getCard(self):
        return self.deck.pop()

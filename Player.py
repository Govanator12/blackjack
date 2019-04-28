from Deck import *

class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []

    def hit(self):
        self.hand.append(deck.getCard)

    def resetPlayer(self):
        self.hand = []

    def getName(self):
        return self.name

    def getHand(self):
        total = 0
        for card in self.hand:
            if isinstance(card, int):
                total += card
            else:
                total += 10

        if 'A' in self.hand:
            if total > 21:
                total -= 9
            else:
                total += 1

        return total if total <= 21 else -1

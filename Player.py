from Deck import *
from Blackjack import *

class Player():

    def __init__(self, name='Player'):
        self.name = name
        self.hand = []

    def hit(self, deck, number_of_cards = 1):
            for n in range(number_of_cards):
                self.hand.append(deck.getCard())

    def resetPlayer(self):
        self.hand = []

    def getName(self):
        return self.name

    def getHand(self):
        return self.hand

    def handValue(self):
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

        return total

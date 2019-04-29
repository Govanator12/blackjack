from Deck import *
from Player import *

class Blackjack():

    def __init__(self):
        self.deck = Deck()
        self.dealer = Player('Dealer')
        self.player = Player()

    # menu function creates the player and starts or quits game

    def menu(self):
        print('Welcome to Blackjack!')
        print('-----------------------')
        ans = (input('Whats your name? ')).title()
        self.player = Player(ans)\

        while True:
            ans = (input(f"Start a new game {self.player.getName()}? (Y/N) ")).lower()

            if ans == 'y':
                Blackjack.play(self)
            elif ans == 'n':
                print('Thanks for playing!')
                break

            else:
                print('Please choose either Y or N\n')

    # play function contains main game loop
    def play(self):
        self.deck.resetDeck()
        self.player.resetPlayer()
        self.dealer.resetPlayer()
        self.player.hit(self.deck, 2)
        self.dealer.hit(self.deck, 2)

        # Assisted mode allows new players to get help when deciding whether to hit or stand
        while True:
            ans = (input('Would you like to play in assisted mode? (Y/N) ')).lower()

            if ans == 'y':
                self.player.setAssistedModeOn()
                break
            elif ans == 'n':
                self.player.setAssistedModeOff()
                break
            else:
                print("Please choose either 'Y' or 'N'")

        while True:
            Blackjack.showHands(self)

            if self.player.handValue() < 21:
                ans = (input('Hit or stand? (H/S)')).lower()

                if ans == 'h':
                    self.player.hit(self.deck)
                elif ans == 's':
                    break
                else:
                    print("Please enter 'H' or 'S'")

            elif self.player.handValue() == 21:
                print('You have 21! Lets see how the dealer does!')
                break
            else:
                break

        Blackjack.showHands(self)

        if self.player.handValue() > 21:
            print('You busted! Better luck next time!')
        else:
            print('The dealer is hitting')
            while self.dealer.handValue() < self.player.handValue():
                self.dealer.hit(self.deck)

                if self.dealer.handValue() > 21:
                    print('The dealer busted!')
                    break
        Blackjack.showHands(self)

        if (self.player.handValue() > self.dealer.handValue() or self.dealer.handValue() > 21) and self.player.handValue() < 21:
            print('Congrats! Youn win!')
        else:
            print('The dealer wins!')

    def showHands(self):
        print(f'\nYour cards {self.player.getHand()}, your total: {self.player.handValue()}')

        if self.player.isAssistedMode():
            print(f'On hit your chance to bust is {Blackjack.chanceToBust(self)}%')

        print(f"Dealer's cards {self.dealer.getHand()}, their total: {self.dealer.handValue()}")

        print('-----------------------------------------------------------\n')

    def chanceToBust(self):
        count = 0

        for card in self.deck.getDeck():
            if isinstance(card, str):
                if self.player.handValue() + 10 > 21:
                    count += 1
            elif card == 'A':
                if self.player.handValue() + 1 > 21:
                    count += 1
            else:
                if self.player.handValue() + card > 21:
                    count += 1
        return int((count/len(self.deck.getDeck()))*100)

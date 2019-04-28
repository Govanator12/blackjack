from Deck import *
from Player import *

class Blackjack():

    def __init__(self):
        pass

    # play function handles game
    def play(self):
        while True:
            print('Welcome to Blackjack!')
            print(-----------------------)
            ans = (input("Start a new game? (Y/N) ")).lower()

            if ans == 'y':
                deck = Deck()
                ans = input('Whats your name? ')
                player = Player(ans)

                while True:
                    pass

            elif ans == 'n':
                print('Thanks for playing!')
                break

            else:
                print('Please choose either Y or N')

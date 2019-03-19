
#text based spades game
from cardDeck import *


class Player():
    def __init__(self, score = 0,):
        self.score = score
        self.hand = []

    def set_bet(self, bet):
        self.bet = bet

    def add(self,x):
        self.hand.append(x)

    def print_hand(self):
        for i in range(len(self.hand)-1):
            print_card(self.hand[i])
            print(', ', end="", flush=True)
        print_card(self.hand[i])
        print('')




def deal_cards(deck, player, comp1, comp2, comp3):
    for i in range(13):
        player.add(draw_card(deck))
        comp1.add(draw_card(deck))
        comp2.add(draw_card(deck))
        comp3.add(draw_card(deck))
    return


if __name__ == '__main__':
    running = True

    while running:
        play = input("Would you like to play Spades? y or n:  ")
        if play == 'y':
            playerName = input("What is your name?  ")
            #deal cards ask user for how many hands
            #create deck
            newdeck = create_deck()
            Player1 = Player()
            Teammate = Player()
            Computer1 = Player()
            Computer2 = Player()
            deal_cards(newdeck,Player1, Teammate, Computer1, Computer2 )

            print(playerName,"'s Cards:")
            Player1.print_hand()

        elif play == 'n':
            print('Thanks for playing spades')
            running = False
        else:
            print('Please enter y or n')
        
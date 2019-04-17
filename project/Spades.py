#text based spades game
from project.cardDeck_print import *

class SpadesGame():
    def __init__(self,playerName):
        self.teams = []
        self.order = []
        self.end_score = 250
        self.turn = 0
        self.startPlayer = 0
        self.won_last = ""
        self.spades_broken = False
        self.card = None
        self.originalSuit = None
        self.teams.append(Team(Player(playerName,False), Player("Teammate",True)))
        self.teams.append(Team(Player("Computer 1",True), Player("Computer 2",True)))
        self.order.append(self.teams[0].players[0])
        self.order.append(self.teams[1].players[0])
        self.order.append(self.teams[0].players[1])
        self.order.append(self.teams[1].players[1])

    def start(self):
        self.start_round()

    def start_round(self):
        self.deck = Deck()
        self.teams[0].deal_cards(self.deck)
        self.teams[1].deal_cards(self.deck)
        self.teams[0].players[0].print_hand()
        #Determine who goes first
        for i in range(4):
            if (self.order[i].has_card(Suit.CLUBS,Card.TWO)):
                self.turn = i
                self.startPlayer = i
        
        self.collect_bets()
        self.play()

    def set_card(self,card):
        if (self.card == None):
            self.originalSuit = card.suit
        self.card = card

    def collect_bets(self):
        self.teams[0].collect_bets()
        self.teams[1].collect_bets()

    def play(self):
        print("")

        curPlayer = self.order[self.turn]
        print(curPlayer.name, "'s turn.")

        if (curPlayer.has_card(Suit.CLUBS,Card.TWO)):
            curPlayer.place_card(self,Suit.CLUBS,Card.TWO)
        else:
            curPlayer.act(self,self.card)

        #Move the turn index to the next player
        self.turn = self.turn + 1
        if (self.turn > 3):
            self.turn = 0

        if (self.turn == self.startPlayer):
            self.end_set()
        else:
            self.play()

    def end_set(self):
        #Reward the book, reset the board, and then call play again
        winner = self.determine_book_winner()
        print(winner.name, " won the hand for their team!")
        print("")
        print("Current Score:")
        print("Team 1: ", self.teams[0].get_score(), " hands")
        print("Team 2: ", self.teams[1].get_score(), " hands")
        print("")

        #Check and make sure players still have cards.. if they don't call end_round
        if (len(winner.hand) > 0) :
            self.turn = self.order.index(winner)
            self.startPlayer = self.turn
            self.card = None
            self.play()
        else:
            self.card = None
            self.end_round()

    def end_round(self):
        self.teams[0].end_round()
        self.teams[1].end_round()

        #Print Score
        print("")
        print("Round Over!  Points Overview:")
        print("Team 1: ", self.teams[0].points, " points")
        print("Team 2: ", self.teams[1].points, " points")
        print("")

        #If either team above score threshhold, and there is no tie they win!
        if (self.teams[0].points > self.teams[1].points and self.teams[0].points > self.end_score):
            print("Team 1 Wins!")
            print("")
            print("")
        elif (self.teams[1].points > self.teams[0].points and self.teams[1].points > self.end_score):
            print("Team 2 Wins!")
            print("")
            print("")
        else:
            self.start_round()


    def determine_book_winner(self):
        val = 0
        winner = None
        for i in range(4):
            if (self.order[i].placedCard.game_value(self.originalSuit) > val):
                val = self.order[i].placedCard.game_value(self.originalSuit)
                winner = self.order[i]
            #self.order[i].placedCard = None
        winner.score = winner.score + 1
        return winner

class Team():
    def __init__(self, player1, player2):
        self.players = []
        self.sandbags = 0
        self.bet = 0
        self.points = 0
        self.players.append(player1)
        self.players.append(player2)

    def deal_cards(self, deck):
        for i in range(13):
            self.players[0].add(deck.draw())
            self.players[1].add(deck.draw())
        self.players[0].sort_hand()
        self.players[1].sort_hand()

    def get_score(self):
        return self.players[0].score + self.players[1].score

    def collect_bets(self):
        i = self.players[0].collect_bet()
        i = i + self.players[1].collect_bet()
        if (self.players[0].isComp == False):
            print("Team 1 anticipates collecting ", i, "hands.  ", self.players[0].name, ": ",self.players[0].bet, "    ",self.players[1].name, ": ",self.players[1].bet)
        else:
            print("Team 2 anticipates collecting ", i, "hands.  ", self.players[0].name, ": ",self.players[0].bet, "    ",self.players[1].name, ": ",self.players[1].bet)
    
    def end_round(self):
        #Calculate Score
        pointDiff = 0
        hands = self.players[0].score + self.players[1].score
        pointDiff = pointDiff + self.account_nil(self.players[0])
        pointDiff = pointDiff + self.account_nil(self.players[1])

        #If you get x more hands than youve bet, you recieve x sandbags
        if (self.bet > hands):
            self.sandbags = self.sandbags + (self.bet - hands)

        #if you get less hands than you've bet you lose 10 * bet in points
        if (hands < self.bet):
            pointDiff = pointDiff - (self.bet * 10)
        else:
            #10 points per hand that you've bet and got
            pointDiff = pointDiff + (hands * 10)

        #If team reaches 10 sandbags, sandbags -> 0 and team loses 100 points
        while (self.sandbags > 10):
            pointDiff = pointDiff - 100
            self.sandbags = self.sandbags - 10

        self.points = self.points + pointDiff
        self.players[0].score = 0
        self.players[1].score = 0

    def account_nil(self,player):
        #If you've elected to go nil, and you (the individual player) has won 0 hands you get 100 points
        #If you've elected to go nil, and you win a hand you lose 100 points
        pointDiff = 0
        if (player.bet == 0):
            if (player.score == 0):
                print(player.name, " successfully went nil and earned 100 points!")
                pointDiff = 100
            elif (player.score > 0):
                print(player.name," tried to go nil and failed, losing the team 100 points!")
                pointDiff = -100
        return pointDiff



class Player():
    def __init__(self, name, computer):
        self.hand = []
        self.name = name
        self.isComp = computer
        self.score = 0

    def act(self,game,curCard):
        validCards = self.get_valid_cards(game,curCard)
        if (self.isComp):
            rand_card = validCards[randint(0, len(validCards)-1)]
            self.place_card(game,rand_card.suit,rand_card.card)
        else:
            #Get player card input on what to play
            print("")
            print("Here are the valid cards you can place:")
            for i in range(len(validCards)):
                print((i+1),": ",validCards[i].string_val())
            print("")
            while True:
                index = input("Which card would you like to play?")
                try:
                    index = int(index)
                    if (index > 0 and index < len(validCards) + 1):
                        break
                except ValueError:
                    pass
            self.place_card(game,validCards[index-1].suit,validCards[index-1].card)


    def place_card(self, game, suit, value):
        card = self.find_card(suit,value)
        if (card != False):
            self.hand.remove(card)
            print(self.name, "Places the ", card.string_val())
            self.placedCard = card
            game.set_card(card)
        else:
            print("Error!")

    def collect_bet(self):
        bet = 0
        if (self.isComp):
            bet = self.calculate_probable_wins()
        else:
             while True:
                bet = input("How many hands do you think you will win? (Betting)")
                try:
                    bet = int(bet)
                    break
                except ValueError:
                    pass
        self.bet = bet
        if (self.bet == 0):
            print(self.name, " is trying to go nil!")
        return bet

    def calculate_probable_wins(self):
        i = 0
        i = i + len(self.find_cards_with_value(Card.ACE))
        i = i + len(self.find_cards_with_value(Card.KING))
        i = i + len(self.find_cards_with_value(Card.QUEEN))
        return i

    def find_card(self, suit, value):
        for i in range(len(self.hand)):
            if (self.hand[i].suit == suit and self.hand[i].card == value):
                return self.hand[i]
        return False
        
    def find_cards(self,suit):
        cards = []
        for i in range(len(self.hand)):
            if (self.hand[i].suit == suit):
                cards.append(self.hand[i])
        return cards

    def find_cards_with_value(self, value):
        cards = []
        for i in range(len(self.hand)):
            if (self.hand[i].card == value):
                cards.append(self.hand[i])
        return cards

    def add(self,x):
        self.hand.append(x)

    def sort_hand(self):
        self.hand.sort(key=lambda x: x.sort_value())

    def has_card(self,suit,card):
        for i in range(len(self.hand)):
            if (self.hand[i].suit == suit and self.hand[i].card == card):
                return True
        return False
        
    def print_hand(self):
        print(self.name,"'s cards")
        for i in range(len(self.hand)-1):
            self.hand[i].print()
            print(', ', end="", flush=True)
        self.hand[len(self.hand)-1].print()
        print('')

    def get_valid_cards(self, game, card):
        validCards = []
        if (card is None):
            validCards.extend(self.find_cards(Suit.CLUBS))
            validCards.extend(self.find_cards(Suit.DIAMONDS))
            validCards.extend(self.find_cards(Suit.HEARTS))
            if (game.spades_broken or len(validCards) == 0):
                validCards.extend(self.find_cards(Suit.SPADES))
        else:
            validCards.extend(self.find_cards(card.suit))
            if (len(validCards) == 0):
                validCards.extend(self.find_cards(Suit.CLUBS))
                validCards.extend(self.find_cards(Suit.DIAMONDS))
                validCards.extend(self.find_cards(Suit.HEARTS))
                validCards.extend(self.find_cards(Suit.SPADES))
        if (len(validCards) == 0):
            validCards = self.hand
        validCards.sort(key=lambda x: x.sort_value())
        return validCards



if __name__ == '__main__':
    running = True

    while running:
        play = input("Would you like to play Spades? y or n:  ")
        if play == 'y' or play == 'Y':
            playerName = input("What is your name?  ")

            #Create Game
            game = SpadesGame(playerName)
            game.start()




        elif play == 'n':
            print('Thanks for playing spades')
            running = False
        else:
            print('Please enter y or n')
        
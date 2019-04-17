from enum import Enum
from enum import IntEnum
from random import *

full_deck = []

class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'



class Deck():
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for card in Card:
                self.cards.append(PlayingCard(Card(card), Suit(suit)))

    def draw(self):
        rand_card = randint(0, len(self.cards)-1)
        return self.cards.pop(rand_card)


class PlayingCard():
    def __init__(self, card_rank, card_suit):
        self.card = card_rank
        self.suit = card_suit

    def sort_value(self):
        i = 0
        if self.suit == Suit.CLUBS:
            i = 14
        elif self.suit == Suit.HEARTS:
            i = 28
        elif self.suit == Suit.DIAMONDS:
            i = 42
        return i + self.card 

    def game_value(self, expectedSuit):
        i = self.card
        if (self.suit == Suit.SPADES):
            i = i + 14
            return i
        elif (self.suit != expectedSuit):
            i = i - 999
        return i

    def string_val(self):
        val = ""
        if self.card < 11:
            val = str(self.card.value)
        elif self.card == 11:
            val = "J"
        elif self.card == 12:
            val = "Q"
        elif self.card == 13:
            val = "K"
        elif self.card == 14:
            val = "A"

        if self.suit.value == 'spades':
            val = val + '♠'
        elif self.suit.value == 'diamonds':
            val = val + '♦'
        elif self.suit.value == 'hearts':
            val = val + '♥' 
        else:
            val = val + '♣'
        return val

    def print(self):
        print(self.string_val(),end="",flush=True)


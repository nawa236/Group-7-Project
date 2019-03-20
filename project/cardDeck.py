from enum import Enum
from enum import IntEnum
from random import *
import pygame

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

class PlayingCard:
    def __init__(self, card_rank, card_suit):
        self.card = card_rank
        self.suit = card_suit

def create_deck():
    for suit in Suit :
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit)))        
    return full_deck

def draw_card(deck):
    rand_card = randint(0, len(deck)-1)
    return deck.pop(rand_card)

def print_card(card):
    if card.card < 11:
        print(card.card.value, end="", flush=True)
    elif card.card == 11:
        print('J', end="", flush=True)
    elif card.card == 12:
        print('Q', end="", flush=True)
    elif card.card == 13:
        print('K', end="", flush=True)
    elif card.card == 14:
        print('A', end="", flush=True)
    if card.suit.value == 'spades':
        print('♠', end="", flush=True)
    elif card.suit.value == 'diamonds':
        print('♦', end="", flush=True)
    elif card.suit.value == 'hearts':
        print('♥', end="", flush=True)
    else:
        print('♣', end="", flush=True)
    return

def disp_card(screen, card, x, y):
    if card.suit.value == 'hearts':
        if card.card == 2:
            cardImg = pygame.image.load('.\JPEG\\2H.jpg')
        elif card.card == 3:
            cardImg = pygame.image.load('.\JPEG\\3H.jpg')
        elif card.card == 4:
            cardImg = pygame.image.load('.\JPEG\\4H.jpg')
        elif card.card == 5:
            cardImg = pygame.image.load('.\JPEG\\5H.jpg')
        elif card.card == 6:
            cardImg = pygame.image.load('.\JPEG\\6H.jpg')
        elif card.card == 7:
            cardImg = pygame.image.load('.\JPEG\\7H.jpg')
        elif card.card == 8:
            cardImg = pygame.image.load('.\JPEG\8H.jpg')
        elif card.card == 9:
            cardImg = pygame.image.load('.\JPEG\9H.jpg')
        elif card.card == 10:
            cardImg = pygame.image.load('.\JPEG\\10H.jpg')
        elif card.card == 11:
            cardImg = pygame.image.load('.\JPEG\JH.jpg')
        elif card.card == 12:
            cardImg = pygame.image.load('.\JPEG\QH.jpg')
        elif card.card == 13:
            cardImg = pygame.image.load('.\JPEG\KH.jpg')
        elif card.card == 14:
            cardImg = pygame.image.load('.\JPEG\AH.jpg')
    elif card.suit.value == 'diamonds':
        if card.card == 2:
            cardImg = pygame.image.load('.\JPEG\\2D.jpg')
        elif card.card == 3:
            cardImg = pygame.image.load('.\JPEG\\3D.jpg')
        elif card.card == 4:
            cardImg = pygame.image.load('.\JPEG\\4D.jpg')
        elif card.card == 5:
            cardImg = pygame.image.load('.\JPEG\\5D.jpg')
        elif card.card == 6:
            cardImg = pygame.image.load('.\JPEG\\6D.jpg')
        elif card.card == 7:
            cardImg = pygame.image.load('.\JPEG\\7D.jpg')
        elif card.card == 8:
            cardImg = pygame.image.load('.\JPEG\8D.jpg')
        elif card.card == 9:
            cardImg = pygame.image.load('.\JPEG\9D.jpg')
        elif card.card == 10:
            cardImg = pygame.image.load('.\JPEG\\10D.jpg')
        elif card.card == 11:
            cardImg = pygame.image.load('.\JPEG\JD.jpg')
        elif card.card == 12:
            cardImg = pygame.image.load('.\JPEG\QD.jpg')
        elif card.card == 13:
            cardImg = pygame.image.load('.\JPEG\KD.jpg')
        elif card.card == 14:
            cardImg = pygame.image.load('.\JPEG\AD.jpg')
    elif card.suit.value == 'spades':
        if card.card == 2:
            cardImg = pygame.image.load('.\JPEG\\2S.jpg')
        elif card.card == 3:
            cardImg = pygame.image.load('.\JPEG\\3S.jpg')
        elif card.card == 4:
            cardImg = pygame.image.load('.\JPEG\\4S.jpg')
        elif card.card == 5:
            cardImg = pygame.image.load('.\JPEG\\5S.jpg')
        elif card.card == 6:
            cardImg = pygame.image.load('.\JPEG\\6S.jpg')
        elif card.card == 7:
            cardImg = pygame.image.load('.\JPEG\\7S.jpg')
        elif card.card == 8:
            cardImg = pygame.image.load('.\JPEG\8S.jpg')
        elif card.card == 9:
            cardImg = pygame.image.load('.\JPEG\9S.jpg')
        elif card.card == 10:
            cardImg = pygame.image.load('.\JPEG\\10S.jpg')
        elif card.card == 11:
            cardImg = pygame.image.load('.\JPEG\JS.jpg')
        elif card.card == 12:
            cardImg = pygame.image.load('.\JPEG\QS.jpg')
        elif card.card == 13:
            cardImg = pygame.image.load('.\JPEG\KS.jpg')
        elif card.card == 14:
            cardImg = pygame.image.load('.\JPEG\AS.jpg')
    elif card.suit.value == 'clubs':
        if card.card == 2:
            cardImg = pygame.image.load('.\JPEG\\2C.jpg')
        elif card.card == 3:
            cardImg = pygame.image.load('.\JPEG\\3C.jpg')
        elif card.card == 4:
            cardImg = pygame.image.load('.\JPEG\\4C.jpg')
        elif card.card == 5:
            cardImg = pygame.image.load('.\JPEG\\5C.jpg')
        elif card.card == 6:
            cardImg = pygame.image.load('.\JPEG\\6C.jpg')
        elif card.card == 7:
            cardImg = pygame.image.load('.\JPEG\\7C.jpg')
        elif card.card == 8:
            cardImg = pygame.image.load('.\JPEG\8C.jpg')
        elif card.card == 9:
            cardImg = pygame.image.load('.\JPEG\9C.jpg')
        elif card.card == 10:
            cardImg = pygame.image.load('.\JPEG\\10C.jpg')
        elif card.card == 11:
            cardImg = pygame.image.load('.\JPEG\JC.jpg')
        elif card.card == 12:
            cardImg = pygame.image.load('.\JPEG\QC.jpg')
        elif card.card == 13:
            cardImg = pygame.image.load('.\JPEG\KC.jpg')
        elif card.card == 14:
            cardImg = pygame.image.load('.\JPEG\AC.jpg')
    cardImg = pygame.transform.scale(cardImg, (50, 100))
    screen.blit(cardImg, (x,y))
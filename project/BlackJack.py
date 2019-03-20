# import the pygame module, so you can use it
import pygame
import time
from cardDeck import *

# initialize the pygame module
pygame.init()


# load and set the logo
logo = pygame.image.load("logo32x32.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Casino Night") 
clock = pygame.time.Clock()
display_height = 800
display_width = 1000
screen = pygame.display.set_mode((display_width, display_height))

def blackjack():
     # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        deckImg = pygame.image.load('./JPEG/red_back.jpg')

        screen.blit(deckImg, (50,50))



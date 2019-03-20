# import the pygame module, so you can use it
import pygame
import time
from cardDeck import *
from menu import *

# initialize the pygame module
pygame.init()


# load and set the logo
logo = pygame.image.load('.\JPEG\KH.jpg')
pygame.display.set_icon(logo)
pygame.display.set_caption("Casino Night") 
clock = pygame.time.Clock()
display_height = 800
display_width = 1000
screen = pygame.display.set_mode((display_width, display_height))

def blackJackButton(screen,msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "draw":
                return True
            elif action == "hold":
                return False
            elif action == "quit":
                main()
                return False
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def blackjack(screen):
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
        #game logic
        deck = create_deck()
        #initial player hand
        plhand = [draw_card(deck), draw_card(deck)]
        plscore = 0
        #player drawing phase
        pdrawing = True
        while pdrawing:
            screen.fill((39, 119, 20))
            deckImg = pygame.image.load('.\JPEG\\red_back.jpg')
            deckImg = pygame.transform.scale(deckImg, (50, 100))
            screen.blit(deckImg, (50,50))
            #display hand
            for p in range(len(plhand)):
                disp_card(screen, plhand[p], (300+(50*p)+1), 800)

            #make buttons
            pdrawing = blackJackButton(screen,"Hit Me",800,450,100,50,(105,105,105),(211,211,211),"draw")
            pdrawing = blackJackButton(screen,"Hold",800,550,100,50,(105,105,105),(211,211,211),"hold")
            pdrawing = blackJackButton(screen,"Quit",800,650,100,50,(105,105,105),(211,211,211),"quit")
            pygame.display.flip()
            clock.tick(60)

    return
# import the pygame module, so you can use it
from pygame import *
import time
from cardDeck import *
from menu import text_objects

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
                return True
            elif action == "quit":
                return True
            elif action == "continue":
                return True
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    return False



def blackjack(screen):
     # define a variable to control the main loop
    running = True
    # main loop
    deckImg = pygame.image.load('.\JPEG\Red_back.jpg')
    deckImg = pygame.transform.scale(deckImg, (50, 100))
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
        dlhand = [draw_card(deck), draw_card(deck)]
        plscore = 0
        #player drawing phase
        pdrawing = True
        while pdrawing:
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                    pdrawing = False

            screen.fill((39, 119, 20))
            screen.blit(deckImg, (50,50))
            #display hands
            for p in range(len(plhand)):
                #print_card(plhand[p])
                disp_card(screen, plhand[p], (300+(75*p)+1), 500)
            for c in range(len(dlhand)):
                disp_card(screen, dlhand[c], (300+(75*c)+1), 50)

            #make buttons
            if blackJackButton(screen,"Hit Me",800,450,100,50,(105,105,105),(211,211,211),"draw"):
                plhand.append(draw_card(deck))
            if blackJackButton(screen,"Hold",800,550,100,50,(105,105,105),(211,211,211),"hold"):
                pdrawing = False
            if blackJackButton(screen,"Quit",800,650,100,50,(105,105,105),(211,211,211),"quit"):
                return

            #calculate player hand score
            plscore = 0
            for p in range(len(plhand)):
                if plhand[p].card.value != 13:
                    plscore += plhand[p].card.value
            #deal with aces
            for p in range(len(plhand)):
                if plhand[p].card.value == 13 and (plscore + 13) <= 21:
                    plscore += plhand[p].card.value
                elif plhand[p] == 13:
                    plscore += 1
            #blackjack or bust
            if plscore >= 21:
                pdrawing = False

            pygame.display.update()  
            clock.tick(30)
        #drawing for dealer if player has not busted
        if plscore <= 21:
            dealdraw = True
            while dealdraw:
                screen.fill((39, 119, 20))
                screen.blit(deckImg, (50,50))
                for event in pygame.event.get():
                    # only do something if the event is of type QUIT
                    if event.type == pygame.QUIT:
                        # change the value to False, to exit the main loop
                        running = False
                        pdrawing = False
                dlscore = 0
                #calculate dealer score
                for d in range(len(dlhand)):
                    if plhand[p].card.value != 13:
                        dlscore += dlhand[p].card.value
                for d in range(len(dlhand)):
                    if dlhand[d].card.value == 13 and (dlscore + 13) <= 21:
                        dlscore += plhand[d].card.value
                    else:
                        dlscore += 1
                #draw if dealer is not tied or greater than player
                if dlscore < plscore:
                    dlhand.append(draw_card(deck))
                else:
                    dealdraw = False

                #
                if blackJackButton(screen,"Quit",800,650,100,50,(105,105,105),(211,211,211),"quit"):
                    print("quit", end="", flush=True)
                    return
                #display hands
                for c in range(len(plhand)):
                    #print_card(plhand[p])
                    disp_card(screen, plhand[c], (300+(75*p)+1), 500)
                for c in range(len(dlhand)):
                    disp_card(screen, dlhand[c], (300+(75*c)+1), 50)

                pygame.display.update()  
                clock.tick(30)

        #results
        dispresults = True
        largeText = pygame.font.Font('freesansbold.ttf',75)
        while dispresults:
            screen.fill((39, 119, 20))
            screen.blit(deckImg, (50,50))
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                    pdrawing = False
            #determine results
            if plscore > 21:
                TextSurf, TextRect = text_objects("You Busted", largeText)
            elif dlscore > 21:
                TextSurf, TextRect = text_objects("You Win (dealer busted)", largeText)
            elif plscore == dlscore:
                TextSurf, TextRect = text_objects("Tie", largeText)
            elif plscore > dlscore:
                TextSurf, TextRect = text_objects("You Win", largeText)
            elif dlscore > plscore:
                TextSurf, TextRect = text_objects("You Lose", largeText)
            else:
                TextSurf, TextRect = text_objects("ERROR", largeText)

            TextRect.center = ((display_width/2),(display_height/2))
            screen.blit(TextSurf, TextRect)
            for c in range(len(plhand)):
                    #print_card(plhand[p])
                    disp_card(screen, plhand[c], (300+(75*p)+1), 500)
            for c in range(len(dlhand)):
                    disp_card(screen, dlhand[c], (300+(75*c)+1), 50)

            if blackJackButton(screen,"CONTINUE",800,450,100,50,(105,105,105),(211,211,211),"continue"):
                dispresults = False
            if blackJackButton(screen,"Quit",800,650,100,50,(105,105,105),(211,211,211),"quit"):
                return
            pygame.display.update()  
            clock.tick(30)
    return
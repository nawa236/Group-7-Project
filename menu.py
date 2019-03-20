# import the pygame module, so you can use it
import pygame
import time

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

# define a main function
def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
    main()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "play":
                BlackJack.blackjack()
            elif action == "settings":
                print("Settings")
            elif action == "quit":
                #vs code errors here, running from .py file quits fine
                pygame.QUIT()     
                quit() 
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def main():
    
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
                
        # create a surface on screen
        screen.fill((39, 119, 20))
        pygame.display.flip()
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Casino Night", largeText)
        TextRect.center = ((display_width/2),(display_height/2 - 200))
        screen.blit(TextSurf, TextRect)

        #add buttons
        button("Play",300,350,400,50,(105,105,105),(211,211,211),"play")
        button("Settings",300,450,400,50,(105,105,105),(211,211,211),"settings")
        button("Quit",300,550,400,50,(105,105,105),(211,211,211),"quit")
    
        
        pygame.display.update()
        clock.tick(15)
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
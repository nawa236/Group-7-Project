#Precondition: You have a certain amount of bets you can place with a certain amount of money
#Postcondition: The amount of money you win is displayed on the screen with all of your winnings
#Purpose: To bet as much money as you have and win as much as possible 




#import your functions needed
from random import *
from math import *


#function1: get_number_to_bet_on()  
#purpose: Asking user for the number they want to bet on
#preconditions: None 
#postconditions: returns integer
#Call the function
def get_a_number_to_bet_on():
    #1. ask the user to enter a bet from 0-36
   
    betnum = input("Below Bet ")
    #x=range(36)
    #while betnum == (0,36):
        #betnum = int(input("What number do you want to bet on? (0-36) "))
    if betnum in range(0,36):
        #2. save this bet for later function
        
        betnum = input("What number do you want to bet on? (0-36) ")
        return betnum
    else:
        #3. if number is not in range ask to bet again
        #print("Bet again")
        betnum = input("What number do you want to bet on? (0-36) ")
         
      
      
    
#function2: get_amount_to_bet
#purpose: asks the user for an amount to bet
#preconditions: = Parameters 
#postconditions: returns integer
#Call the function
def get_amount_to_bet(pot):
    #1. ask user for a bet amount
    bet=int(input("How much do you want to bet ? "))
    while bet == (0,pot):
        bet=int(input("How much do you want to bet ? "))
    if bet in range(0,pot):
        return bet
    #2. continue if bet is in range if it is not tell the user it isnt
    while bet not in range(0,pot):
        print("That is too much!")
        #3. ask the user again for a bet in range
        bet=int(input("How much do you want to bet ? "))
    return bet
            
        
        
       
#function3: get_choice
#purpose: offers the user a choice of two characters or N, with a label and returns the character they entered
#preconditions: = 3 choices that the user can pick from some of the bets 
#postconditions: returns only the upper case letters         
#Call the function
def get_choice(firstchoice,secondchoice,c):
    #1. ask user to choose what they want
    inputstring= ("Do you want to bet on " + c)  
    #2. all of the inputs should be returned as upper case with x.upper()
    choice = input(inputstring).upper()
    while choice != firstchoice  and choice != secondchoice and choice  != "N":
        print("Not a valid answer")
        choice = input(inputstring).upper()
    #Return choice for later
    return(choice)
        
        


#function4: get_randnum()
#purpose: this function will call the random number generator to get a random number in the right range
#preconditions: = Parameters 
#postconditions: returns an integer
#Call the function
def get_randnum():
    #2. get the random input from there bets
    random=randrange(0,37)
    return random




#function5: display_spin
#purpose: This will display the number the ball lands on 
#preconditions: = Random number generated  
#postconditions: returns integer 
#Call the function
def display_spin (random):
    #1. Once the random number is generated display the display_spin
    print("Spinning ... .1. 2. 3. 4... And the number is ",random)
    
    


#function6: get_and_report_winnings
#purpose: this function will return the amount the player won 
#preconditions: = Parameters 
#postconditions: returns values, output, changes to parameter
#Call the function
def get_and_report_winnings(bet,betnum,pot,random,firstchoice,secondchoice,thirdchoice,choice):
    tot=0
    if betnum == random:
        tot += bet *5
        #1. Tell the user the amount of winning they win
        print("You win 5 times your bet! You hit the number!",tot)
    else:
        #2. if you did not win display no penalty
        print("You did not get the number no penalty ")
        
    if firstchoice != "N":
        #3.0 Display if it was even or odd
        #3.1 if even or odd add 2 x to your bet
        if (random % 2 == 0  and firstchoice == 'E') or (random % 2 == 1 and firstchoice == "O"):
            tot+= 2 * bet
            firstchoice= 2 * bet
            print("You win two times your bet on odd/even! ", firstchoice)
        else: 
            #3.2 if else take bet amount away from your pot
            tot-= bet
            firstchoice = bet
            print("you lost your bet on odd or even.",firstchoice)
    #4.0 Display if it was red/black        
    if secondchoice != "N":
        if (random % 3 == 0 and secondchoice == 'R') or (random % 3 > 0 and secondchoice == "B"):
            #4.1 if red or black add 3 x your bet
            tot+= 3 * bet
            secondchoice = 3 * bet
            print("You won three times your bet on red/black!",tot)
        else:
            #4.2 if else take bet amount away from your pot
            tot-= 2 * bet
            secondchoice= 2 * bet
            print("You lose 2 times your bet.",secondchoice)
    #5.0 Display if it was high, low or no bet
    if thirdchoice != "N":
        #5.1 if number<=18 then low if number>18 then high
        if (random > 18 and thirdchoice == "H") or (random < 18 and thirdchoice == "L"):
            #5.2 if you win high or low add bet amount to pot
            tot+= bet
            thirdchoice= bet
            print("You win your bet", thirdchoice)
        else: 
            #5.3 if else subtract bet amount from pot
            tot-= bet
            thirdchoice= bet
            print("You lost your bet on high/low", thirdchoice)
    return tot
            
        
            
        
#function7: get_y_or_n ()
#purpose: this function asks the user a question about playing again and returns either an uppercase y or an uppercase n
#preconditions: = No Parameters 
#postconditions: returns has to be uppercase y or uppercase n
#Call the function
def get_y_or_n():
    #1.Display "Do you want to play again?" 
    play=input("Do you want to play again? (y/n) ").upper()
    #2. choices of (y/n)
    while play != 'N' and play!= 'Y':
        #3. display choice of y/n if not a answer
        print("Not a answer")
        play=input("Do you want to play again? (y/n) ").upper()
    return play
        
        
        







#1. Main function "def main:()"
def main ():
    print()
    #2. display introductory message Spin and win! Big Blue Roulette!!!
    print("Spin and Win!!! Big Blue Roulette!!!")
    #2.1 Dispay how much money they have "$100"
    pot= 100
    end= "Y"
    #3. Tell user how much there pot is
    print("Your pot is ","$",pot,sep="")
    print()    
    #3.1 initialize pot, play flag
    while pot>0 and end == "Y":
        #4. Ask the user what number they want to bet on
        betnum = get_a_number_to_bet_on()
        #5. Call get_amount_to_bet
        bet=get_amount_to_bet(pot)
        #6. Call get_choice to offer them even/odd/no bet
        firstchoice = get_choice("E", "O","even/odd/no bet? (E/O/N) ")
        #7. Call get_choice to offer them red/black/no bet (R/B/N)
        secondchoice = get_choice("R","B", "red/black/no bet? (R/B/N) ")
        #8. Call get_choice to offer them high/low/no bet
        thirdchoice = get_choice("H","L","high/low/no bet? (H/L/N ")
        #9. Call get_randnum() to get the random integer of there bets
        random = get_randnum()
        print()
        #10. Call display_spin to display the random number
        display_spin(random)      
        print()
        #11. After all the bets display total amount of pot after all of wins
            # and losses have been calculated. You win $....(amount)
                #11.1 Report total winnings        
        tot = get_and_report_winnings(bet,betnum,pot,random,firstchoice,secondchoice,thirdchoice,choice)
        pot = pot + tot
        print("Now you have $",pot)
        print()
        #12.0 If pot is less then 0 game is over
        if pot < 0:
            end = get_y_or_n() 
        else:
            #12.1 Call get_y_or_n ()
            end = get_y_or_n()
    #13.0 Display you left the game with $(amount) because you quit
    print("Thanks for playing! You left the game with $", pot)
    print()
        
#14. End with main         
main()

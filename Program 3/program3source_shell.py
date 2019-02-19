# Kyle James, kjja223@g.uky.edu
# 10/31/13, Section 14
# 
# Purpose:
#     A dice game that interacts with the user IN THE PYTHON SHELL. An initial die is rolled,
#     and the player continues to acquire money based on the number rolled until they decide
#     to quit the game and leave with the money they earned, or they roll the number initially
#     rolled - in which case they lose all their money and the game is over.
# 
# Preconditions:
#     -Initial die rolled
#     -User earns amount of roll
#     -User asked to roll again
# 
# Postconditions: 
#     -User either: -Leaves game before rolling die identical to first roll with all money
#                   -Rolls die identical to first roll, loses all money and game is over
# 
####
# Design:
# 1.0 print intro message
# 2.0 simulate first die roll, print the roll, and assign money won to amount of the roll
# 3.0 print message for user detailing how to continue game, await user input
# 4.0 assign Boolean variable gameOver to False, to flag when the user loses the game by rolling the same number
# 5.0 while the user chooses to continue the game, indicated by a 'y' or 'Y' response, and the user has not lost the game:
#     5.1 simulate and display a die roll
#     5.2 if the die roll is not equal to the first roll
#         5.2.1 add new die roll to total amount won
#         5.2.2 print amount won on roll and total amount won to user
#         5.3.3 ask user if they want to roll again, await user input
#     5.3 else
#         5.3.1 gameOver is set to True to indicate the user has lost the game
#         5.3.2 print message detailing the loss to the user
# 6.0 if gameOver variable is set to False after while loop, indicating user choosing to exit game:
#     6.1 print total amount won by the user


from random import randrange #used for randon number generator simulating roll of a die

# get_a_roll
# Purpose: Simulate one roll of a six-sided die
# Preconditions: None
# Postconditions: One random number between 1 and 6 inclusive returned
# Design: 1.0 return random number from 1 to 6 inclusive
def get_a_roll():
  return randrange(1,7)

# display_die
# Purpose: Displays the face of a six-sided die based on integer passed as a parameter
# Preconditions: Positive integer from 1 to 6 inclusive passed as a parameter
# Postconditions: Appropriate die face drawn to shell/graphics window
# Design: 1.0 if number parameter is equal to 1
#             1.1 draw 1-face of a die
#         2.0 else if number is equal to 2
#             2.1 draw 2-face of a die
#         3.0 else if number is equal to 3
#             3.1 draw 3-face of a die
#         4.0 else if number is equal to 4
#             4.1 draw 4-face of a die
#         5.0 else if number is equal to 5
#             5.1 draw 5-face of a die
#         6.0 else (acts as case for 6 and all other integers)
#             6.1 draw 6-face of a die
def display_die(num):
  if num == 1:
    draw_1()
  elif num == 2:
    draw_2()
  elif num == 3:
    draw_3()
  elif num == 4:
    draw_4()
  elif num == 5:
    draw_5()
  else:
    draw_6()

# draw_<num> (draw_1, draw_2, etc.)
# Purpose: Outputs corresponding face of a die to the screen for the user
# Preconditions: None
# Postconditions: Die face corresponding to function name output to screen
# Design: 1.0 Print/Display die face to screen (return nothing)
def draw_1():
  print("+---+")
  print("|   |")
  print("| * |")
  print("|   |")
  print("+---+")

def draw_2():
  print("+---+")
  print("|*  |")
  print("|   |")
  print("|  *|")
  print("+---+")

def draw_3():
  print("+---+")
  print("|*  |")
  print("| * |")
  print("|  *|")
  print("+---+")
  
def draw_4():
  print("+---+")
  print("|* *|")
  print("|   |")
  print("|* *|")
  print("+---+")
 
def draw_5():
  print("+---+")
  print("|* *|")
  print("| * |")
  print("|* *|")
  print("+---+")

def draw_6():  
  print("+---+")
  print("|* *|")
  print("|* *|")
  print("|* *|")
  print("+---+")
  
def main():
  #prints opening message
  print("The game of \'Don't Match\'\n")
  
  #simulates first roll, and adds amount of roll to total money earned  
  firstRoll = get_a_roll()
  total = firstRoll
  
  #prints roll to user alone with die face, and print instructions as to how
  #to continue the game as well as the total money won so far
  print("Your first roll is",firstRoll)
  display_die(firstRoll)
  print("You can roll as long as you don't roll another",firstRoll)
  print("\n You have $",total,sep="")
  
  #gathers input from user to determine if they wish to continue the game
  choice = input("\nDo you want to roll again? (y/n) ")
  
  #initializes gameOver flag to False to check to see if the user loses the game
  gameOver = False  
  
  #while the user continues to play the game indicated by a 'y' response and hasn't lost, the game
  #simulates and displays a roll to the user
  while (choice == "y" or choice == "Y") and gameOver == False:
    roll = get_a_roll()
    display_die(roll)
    #if the roll is not the same as the first roll, the user adds the amount of the roll
    #onto their total and is informed of their winnings on the turn, and 
    #asked if they wish to play again
    if roll != firstRoll:
      total += roll
      print("You won $",roll,sep="")
      print(" You have $",total,sep="")
      choice = input("\nDo you want to roll again? (y/n) ")
    #if the roll is the same as the first roll, the user loses the game. gameOver is set
    #to True to indicate a lost game, which causes the program
    #to exit the loop without furthur user input. The user is informed of the loss via print statement
    else:
      gameOver = True
      print("You matched! You lost all your money!\nsorry!")
  
  #if gameOver was not changed to True (indicating the user left the game without losing),
  #the total winnings are printed for the user at the end of the game
  if gameOver == False:
    print("You left with $",total,sep="")

main()
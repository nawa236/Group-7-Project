# Kyle James, kjja223@g.uky.edu
# Section 14, 11/5/13
# 
# Purpose:
#     A dice game that interacts with the user in a graphics window. An initial die is rolled,
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
# 1.0 import graphics and random number libraries
# 2.0 create graphics window with title
# 3.0 create and draw title, "Yes" and "No" buttons to window
# 4.0 simulate first die roll and display it on the graphics window
# 5.0 display initial instructions and total money won (equal to first roll)
# 6.0 create winnings text (set to empty string) for future successful rolls
# 7.0 display message for user detailing how to continue game, pause for user input
# 8.0 assign user click to variable, determine if user clicked the yes button
# 9.0 assign Boolean variable gameOver to False, to flag when the user loses the game by rolling the same number
# 10.0while the user chooses to continue the game, indicated by clicking the "Yes" button, and
#     the user has not lost the game, indicated by gameOver being True:
#     10.1 simulate and display a die roll
#     10.2 if the die roll is not equal to the first roll
#         10.2.1 add new die roll to total amount won
#         10.2.2 redisplay amount won on roll and total amount won to user
#         10.3.3 ask user if they want to roll again, pause for user input
#         10.3.4 redetermine if user clicked the yes button
#     10.3 else
#         10.3.1 undraw "Yes" and "No" buttons preventing continuation of the game
#         10.3.2 gameOver is set to True to indicate the user has lost the game
#         10.3.3 display message detailing the loss to the user
# 11.0if gameOver variable is set to False after while loop, indicating user choosing to exit game:
#     11.1 undraw "Yes" and "No" buttons from screen
#     11.2 set current winnings text to total winnings the user left with
# 12.0display "click to exit" message, pause for user click, close window

# get_a_roll
# Purpose: Simulate one roll of a six-sided die
# Preconditions: None
# Postconditions: One random number between 1 and 6 inclusive returned
# Design: 1.0 return random number from 1 to 6 inclusive
def get_a_roll():
  return randrange(1,7)

# display_die
# Purpose: Displays the face of a six-sided die based on integer passed as a parameter
# Preconditions: -Positive integer from 1 to 6 inclusive passed as a parameter
#                -Valid Point object passed as a parameter within graphics window bounds
#                -Valid graphics window passed as parameter
# Postconditions: Appropriate die face drawn to graphics window
# Design: 1.0 if number parameter is equal to 1
#             1.1 draw 1-face of a die to graphics window
#         2.0 else if number is equal to 2
#             2.1 draw 2-face of a die to graphics window
#         3.0 else if number is equal to 3
#             3.1 draw 3-face of a die to graphics window
#         4.0 else if number is equal to 4
#             4.1 draw 4-face of a die to graphics window
#         5.0 else if number is equal to 5
#             5.1 draw 5-face of a die to graphics window
#         6.0 else (acts as case for 6 and all other integers)
#             6.1 draw 6-face of a die to graphics window
def display_die(point,num,win):
  if num == 1:
    Image(point,"one.gif").draw(win)
  elif num == 2:
    Image(point,"two.gif").draw(win)
  elif num == 3:
    Image(point,"three.gif").draw(win)
  elif num == 4:
    Image(point,"four.gif").draw(win)
  elif num == 5:
    Image(point,"five.gif").draw(win)
  else:
    Image(point,"six.gif").draw(win)

# clickedYes
# Purpose: Determines if the user clicks within the bounds of the yes button
#          in this program or not.
# Preconditions: Valid floats containing x- and y- coordinates of click passed as parameters
# Postconditions: String containing 'y' or 'n' returned
# Design: 1.0 if x-coord and y-coord are between bounds of box
#             1.1 return 'y'
#         2.0 else
#             2.1 return 'n'
def clickedYes(xcoord,ycoord):
  if 275 <= xcoord <= 325 and 350 <= ycoord <= 400:
    return 'y'
  else:
    return 'n'
  
#import statements for graphics functions and random number generator
from graphics import *
from random import randrange
  
def main():
  #creates window and draws title text and yes/no buttons on the screen
  win = GraphWin("Don't Match!!",500,500)
  title_text = Text(Point(250,10),"The game of \'Don't Match\'")
  title_text.draw(win)

  #simulates the first die roll before user interaction. Displays text containing rules,
  #rules of the game, and the user's total (set to the amount of the first roll)
  #to the user, as well as calling the display_die function to display the correct die.
  firstRoll = get_a_roll()
  firstRoll_text = Text(Point(350,150),"Your first roll is " + str(firstRoll))
  firstRoll_text.draw(win)
  rules_text = Text(Point(325,200),"You can roll as long as you don't roll another " + str(firstRoll))
  rules_text.draw(win)
  total = firstRoll
  total_text = Text(Point(325,250),"You have $" + str(total))
  total_text.draw(win)
  display_die(Point(55,200),firstRoll,win)
  
  #creates text for winnings earned on the turn. Set to empty string originally, and
  #replaced when the user successfully completes a turn.
  winnings_text = Text(Point(350,475),"")
  winnings_text.draw(win)
  
  #creates and displays yes/no buttons for the user to control user interactivity, and
  #prompt for user to click these buttons depending on their wishes.
  continue_text = Text(Point(350,300),"Do you want to roll again?")
  continue_text.draw(win)
  yesbutton_box = Rectangle(Point(275,350),Point(325,400))
  yesbutton_box.draw(win)
  yesbutton_text = Text(Point(300,375),"YES")
  yesbutton_text.draw(win)
  nobutton_box = Rectangle(Point(350,350),Point(400,400))
  nobutton_box.draw(win)
  nobutton_text = Text(Point(375,375),"NO")
  nobutton_text.draw(win)  
  
  #with all instructions displayed, the program pauses for a user click and stores
  #it for testing whether the use chose to continue.
  click = win.getMouse()
  #calls clickedYes function to determine if click is within bounds of yes button or not
  clickString = clickedYes(click.getX(),click.getY())
  
  #initializes a Bool flag to False, becomes True if/when the user loses the game later in the loop.
  gameOver = False

  #while the user continues to play the game, indicated by clicking inside the "Yes" button bound:
  while clickString == 'y' and gameOver == False:
    #simulates and displays another die roll
    roll = get_a_roll()
    display_die(Point(55,400),roll,win)
    #if new roll is not the same as the first, total is updated, winnings on the turn
    #are displayed, and program pauses to reassign click depending on user choice.
    if roll != firstRoll:
      total += roll
      total_text.setText("You have $" + str(total))
      winnings_text.setText("You won $" + str(roll))
      click = win.getMouse()
      clickString = clickedYes(click.getX(),click.getY())
    #otherwise, user loses the game. gameOver is flagged to True, yes/no buttons and text disappear,
    #and turn winnings text is replaced by a consoling message. Loop is exited immediately after.
    else:
      gameOver = True
      continue_text.undraw()
      yesbutton_box.undraw()
      yesbutton_text.undraw()
      nobutton_box.undraw()
      nobutton_text.undraw()
      winnings_text.undraw()
      sorry_text1 = Text(Point(350,450),"Sorry!")
      sorry_text1.draw(win)
      sorry_text2 = Text(Point(350,475),"You matched! You lost all your money!")
      sorry_text2.draw(win)

  #if the user chose to leave the game before losing, a message showing their final
  #winnings is displayed at the bottom of the screen. Yes/no buttons and text disappear.
  if gameOver == False:
    winnings_text.setText("You left with $" + str(total))
    continue_text.undraw()
    yesbutton_box.undraw()
    yesbutton_text.undraw()
    nobutton_box.undraw()
    nobutton_text.undraw()    

  #pauses for user click, and closes the window to end the program  
  end_text = Text(Point(350,495),"Click to exit")
  end_text.draw(win)
  win.getMouse()
  win.close()

main()
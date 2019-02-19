# Team 5, Section 14
# 10/30/13
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
# 1.0 create graphics window with title
# 2.0 create and draw title, "Yes" and "No" buttons to window
# 3.0 simulate first die roll and display it on the graphics window
# 4.0 display initial instructions and total money won (equal to first roll)
# 5.0 display message for user detailing how to continue game, pause for user input
# 6.0 assign Boolean variable gameOver to False, to flag when the user loses the game by rolling the same number
# 7.0 while the user chooses to continue the game, indicated by clicking the "Yes" button:
#     7.1 simulate and display a die roll
#     7.2 if the die roll is not equal to the first roll
#         7.2.1 add new die roll to total amount won
#         7.2.2 redisplay amount won on roll and total amount won to user
#         7.3.3 ask user if they want to roll again, pause for user input
#     7.3 else
#         7.3.1 undraw "Yes" and "No" buttons preventing continuation of the game
#         7.3.2 gameOver is set to True to indicate the user has lost the game
#         7.3.3 display message detailing the loss to the user
# 8.0 if gameOver variable is set to False after while loop, indicating user choosing to exit game:
#     8.1 display message with total amount won
# 9.0 pause for click, close graphics window

# get_a_roll
# Purpose: Simulate one roll of a six-sided die
# Preconditions: None
# Postconditions: One random number between 1 and 6 inclusive returned
# Design: 1.0 return random number from 1 to 6 inclusive

# display_die
# Purpose: Displays the face of a six-sided die based on integer passed as a parameter
# Preconditions: Positive integer from 1 to 6 inclusive passed as a parameter
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
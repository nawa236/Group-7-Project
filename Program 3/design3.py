# Kyle James, kjja223@g.uky.edu
# 10/26/13, Section 14
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
# 5.0 while the user chooses to continue the game, indicated by a 'y' or 'Y' response:
#     5.1 simulate and display a die roll
#     5.2 if the die roll is not equal to the first roll
#         5.2.1 add new die roll to total amount won
#         5.2.2 print amount won on roll and total amount won to user
#         5.3.3 ask user if they want to roll again, await user input
#     5.3 else
#         5.3.1 choice variable is set to string other than 'y' or 'Y' to exit while loop
#         5.3.2 gameOver is set to True to indicate the user has lost the game
#         5.3.3 print message detailing the loss to the user
# 6.0 if gameOver variable is set to False after while loop, indicating user choosing to exit game:
#     6.1 print total amount won by the user

# get_a_roll
# Purpose: Simulate one roll of a six-sided die
# Preconditions: None
# Postconditions: One random number between 1 and 6 inclusive returned
# Design: 1.0 return random number from 1 to 6 inclusive

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

# draw_<num> (draw_1, draw_2, etc.)
# Purpose: Outputs corresponding face of a die to the screen for the user
# Preconditions: None
# Postconditions: Die face corresponding to function name output to screen
# Design: 1.0 Print/Display die face to screen (return nothing)
# My different and overall terrible rendition of program 3
# Kyle James, 10/21/13

from graphics import *
from random import *

win = GraphWin("Kyle's Shitty Dice Game",500,500)
win.setCoords(-250,-250,250,250)
dotMiddle = Circle(Point(0,0),10)
dotMiddle.setFill("black")
dotTopLeft = Circle(Point(-75,75),10)
dotTopLeft.setFill("black")
dotTopRight = Circle(Point(75,75),10)
dotTopRight.setFill("black")
dotBotLeft = Circle(Point(-75,-75),10)
dotBotLeft.setFill("black")
dotBotRight = Circle(Point(75,-75),10)
dotBotRight.setFill("black")
dotMidLeft = Circle(Point(-75,0),10)
dotMidLeft.setFill("black")
dotMidRight = Circle(Point(75,0),10)
dotMidRight.setFill("black")

def drawroll(num):
  if num == 1:
    dotMiddle.draw(win)
  elif num == 2:
    dotTopLeft.draw(win)
    dotBotRight.draw(win)
  elif num == 3:
    dotTopLeft.draw(win)
    dotMiddle.draw(win)
    dotBotRight.draw(win)
  elif num == 4:
    dotTopLeft.draw(win)
    dotTopRight.draw(win)
    dotBotLeft.draw(win)
    dotBotRight.draw(win)
  elif num == 5:
    dotTopLeft.draw(win)
    dotTopRight.draw(win)
    dotBotLeft.draw(win)
    dotBotRight.draw(win)
    dotMiddle.draw(win)
  else:
    dotTopLeft.draw(win)
    dotTopRight.draw(win)
    dotBotLeft.draw(win)
    dotBotRight.draw(win)
    dotMidLeft.draw(win)
    dotMidRight.draw(win)
  
def undrawroll(num):
  if num == 1:
    dotMiddle.undraw()
  elif num == 2:
    dotTopLeft.undraw()
    dotBotRight.undraw()
  elif num == 3:
    dotTopLeft.undraw()
    dotMiddle.undraw()
    dotBotRight.undraw()
  elif num == 4:
    dotTopLeft.undraw()
    dotTopRight.undraw()
    dotBotLeft.undraw()
    dotBotRight.undraw()
  elif num == 5:
    dotTopLeft.undraw()
    dotTopRight.undraw()
    dotBotLeft.undraw()
    dotBotRight.undraw()
    dotMiddle.undraw()
  else:
    dotTopLeft.undraw()
    dotTopRight.undraw()
    dotBotLeft.undraw()
    dotBotRight.undraw()
    dotMidLeft.undraw()
    dotMidRight.undraw()

def yesButtonClicked(x,y):
  if -125 <= x <= -25 and -225 <= y <= -175:
    return True
  else:
    return False
  
def noButtonClicked(x,y):
  if 125 >= x >= 25 and -225 <= y <= -175:
    return True
  else:
    return False

def main():
  titleText = "Click anywhere to roll that suckah"
  title = Text(Point(0,225),titleText)
  title.draw(win)
  win.getMouse()
  
  roll = randrange(1,7)
  firstRoll = roll
  rollCounter = 1
  gameover = False
  cashMoney = roll
  drawroll(roll)
  
  diceBody = Rectangle(Point(-125,-125),Point(125,125))
  diceBody.draw(win)
  yesButton = Rectangle(Point(-125,-225),Point(-25,-175))
  yesButton.setFill("green")
  yesButton.draw(win)
  yesClicked = False
  noButton = Rectangle(Point(25,-225),Point(125,-175))
  noButton.setFill("red")
  noButton.draw(win)
  noClicked = False
  yesText = Text(Point(-75,-200),"Yes!")
  yesText.draw(win)
  noText = Text(Point(75,-200),"Hell naw!")
  noText.draw(win)
  cashMoney_Text = Text(Point(0,200),"Current Ca$hM0neyz: "+str(cashMoney))
  cashMoney_Text.setFill("blue")
  cashMoney_Text.draw(win)
  rollCounter_Text = Text(Point(0,175),"You have survived "+str(rollCounter)+" rolls.")
  rollCounter_Text.draw(win)
  title.setText("You cannot roll a "+str(roll)+" now. Roll again?")
  currentRoll_Text = Text(Point(0,150),"You just rolled a "+str(roll)+".")
  currentRoll_Text.draw(win)
  while noClicked == False and yesClicked == False:
    pointClicked = win.getMouse()
    noClicked = noButtonClicked(pointClicked.getX(),pointClicked.getY())
    yesClicked = yesButtonClicked(pointClicked.getX(),pointClicked.getY())
    if noClicked == True:
      undrawroll(roll)
      diceBody.undraw()
      title.undraw()
      yesButton.undraw()
      yesText.undraw()
      noButton.undraw()
      noText.undraw()
      cashMoney_Text.setText("Total Ca$hM0neyz: "+str(cashMoney))
      deadMansText = Text(Point(0,0),"GAME OVER D:")
      deadMansText.setSize(24)
      deadMansText.draw(win)
      closeText = Text(Point(0,-100),"Click anywhere to close")
      closeText.setFill("red")
      closeText.draw(win)
      win.getMouse()
      win.close()
      gameover = True

  undrawroll(roll)  
  roll = 0
  while roll != firstRoll and gameover != True:
    yesClicked = False
    noClicked = False    
    undrawroll(roll)
    roll = randrange(1,7)
    drawroll(roll)
    currentRoll_Text.setText("You just rolled a "+str(roll)+".")
    if roll == firstRoll:
      undrawroll(roll)
      diceBody.undraw()
      yesButton.undraw()
      yesText.undraw()
      noButton.undraw()
      noText.undraw()      
      title.setText("You rolled a "+str(roll)+" goddamnit YOU HAD ONE JOB!")
      cashMoney_Text.setText("Total Ca$hM0neyz: 0")
      deadMansText = Text(Point(0,0),"GAME OVER D:")
      deadMansText.setSize(24)
      deadMansText.draw(win)
      closeText = Text(Point(0,-100),"Click anywhere to close")
      closeText.setFill("red")
      closeText.draw(win)
      win.getMouse()
      win.close()
      gameover = True
    cashMoney += roll
    rollCounter += 1
    cashMoney_Text.setText("Current Ca$hM0neyz: "+str(cashMoney))
    rollCounter_Text.setText("You have survived "+str(rollCounter)+" rolls.")
    while noClicked == False and yesClicked == False and gameover == False:
      pointClicked = win.getMouse()
      noClicked = noButtonClicked(pointClicked.getX(),pointClicked.getY())
      yesClicked = yesButtonClicked(pointClicked.getX(),pointClicked.getY())
      if noClicked == True:
        undrawroll(roll)
        diceBody.undraw()
        title.undraw()
        yesButton.undraw()
        yesText.undraw()
        noButton.undraw()
        noText.undraw()        
        cashMoney_Text.setText("Total Ca$hM0neyz: "+str(cashMoney))
        deadMansText = Text(Point(0,0),"GAME OVER D:")
        deadMansText.setSize(24)
        deadMansText.draw(win)
        closeText = Text(Point(0,-100),"Click anywhere to close")
        closeText.setFill("red")
        closeText.draw(win)
        win.getMouse()
        win.close()
        gameover = True
  
main()
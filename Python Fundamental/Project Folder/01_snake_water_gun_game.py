"""
1 for snake  
-1 for water
0 for gun 

"""

import random

computerChoice = random.choice([1, -1, 0])
userInput = input("Enter s or w or g: ")
choiceDict = {"s":1, "w":-1, "g":0}

userChoice = choiceDict[userInput]

reverseDict = {1:"snake", -1:"water", 0:"gun"}

print(f"You choose {reverseDict[userChoice]}\nComputer's choose {reverseDict[computerChoice]}")

if(computerChoice == userChoice):
  print("Match Tied!!")

else:
  if(computerChoice == 1 and userChoice == -1):
    print("You loss! Computer Win")
  elif (computerChoice == 1 and userChoice == 0):
    print("You win") 
  elif (computerChoice == -1 and userChoice == 1):
    print("You win") 
  elif (computerChoice == -1 and userChoice == 0):
    print("You loss! Computer Win") 
  elif (computerChoice == 0 and userChoice == 1):
    print("You loss! Computer Win") 
  elif (computerChoice == 0 and userChoice == -1):
    print("You win")
  else:
    print("something went wrong!!!")




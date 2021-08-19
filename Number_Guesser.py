#Number Guesser
import random
randomNum = random.randrange(0, 100)
chance = 0
while(True):
  try:
    user_choice = int(input(""))
    if randomNum == user_choice:
      print("You has guessed right number")
      chance += 1
      print("You have guessed in ", chance, "chances")
      exit()
    elif randomNum > user_choice:
      print("little greater")
      chance += 1  
    elif randomNum < user_choice:
      print("little smaller")
      chance += 1 
  except:
    print("Enter valid integer number")

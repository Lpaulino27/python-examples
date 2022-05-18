import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
userSel = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if userSel >= 3 or userSel < 0:
  print("You typed an invalid number, you lose!")
else:
  #Printing user's selection
  print(game_images[userSel])
  
  #Printing computer's selection
  compSel = random.randint(0, 2)
  print(f"Computer chose {str(compSel)}:")
  
  print(game_images[compSel])
  
  #Looking for the winner
  result = ""
  if userSel == 0:
    if compSel == 0:
      result = "It's a draw"
    elif compSel == 1:
      result = "You lose"
    elif compSel == 2:
      result = "You win"
  elif userSel == 1:
    if compSel == 0:
      result = "You win"
    elif compSel == 1:
      result = "It's a draw"
    elif compSel == 2:
      result = "You lose"
  elif userSel == 2:
    if compSel == 0:
      result = "You lose"
    elif compSel == 1:
      result = "You win"
    elif compSel == 2:
      result = "It's a draw"
  
  print(result)
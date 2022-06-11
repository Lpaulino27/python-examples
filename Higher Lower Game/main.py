from turtle import clear
from game_data import data
from art import logo, vs
import random

score = 0

def getAccountInfo():
    '''To get account information'''
    return random.choice(data)

def formatAccountInfo(account):
    '''To format account information'''
    return account["name"] + ", " + account["description"] + ", " + account["country"] + "."

def compareFollowers(accFolA, accFolB):
    if accFolA > accFolB:
        return "A"
    else:
        return "B"

def game():
    ''' Main function to start the game '''
    account = ""


    #Printing the starting logo
    print(logo)
    
    #Getting and printing account A random information
    account = getAccountInfo()
    follower_count_A = account["follower_count"]
    print("Compare A: " + formatAccountInfo(account))

    #Printing the VS logo
    print(vs)
    
    #Getting and printing account B random information
    account = getAccountInfo()
    follower_count_B = account["follower_count"]
    print("Compare B: " + formatAccountInfo(account))

    #Asking for an answer and making the comparison
    userChoosed = input("Who has more followers? Type 'A' or 'B': ")
    accountWinner = compareFollowers(follower_count_A, follower_count_B)

    #Checking the result
    if userChoosed.upper() == accountWinner.upper():
        return True
    else:
        return False

#Starting the game
bResult = game()

print(bResult)
#Count points and show results
while bResult == True: 
    score += 1
    clear()
    print(f"You're right! Current score: {score}")
    bResult = game()
else:
    clear()
    print(f"Sorry, that's wrong. Final score: {score}")
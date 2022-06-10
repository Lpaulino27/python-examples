from turtle import clear
from game_data import data
from art import logo, vs
import random

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
    score = 0

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

    clear()
    
    if userChoosed == accountWinner:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

    print(userChoosed.upper())
    print(follower_count_A)
    print(follower_count_B)
    print(compareFollowers(follower_count_A, follower_count_B))

game()
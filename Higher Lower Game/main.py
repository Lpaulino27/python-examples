from turtle import clear
from game_data import data
from art import logo, vs
import random

score = 0


def get_account_info():
    """To get account information"""
    return random.choice(data)


def format_account_info(account):
    """To format account information"""
    return account["name"] + ", " + account["description"] + ", " + account["country"] + "."


def compare_followers(acc_fol_a, acc_fol_b):
    if acc_fol_a > acc_fol_b:
        return "A"
    else:
        return "B"


def game():
    """ Main function to start the game """
    account = ""

    # Printing the starting logo
    print(logo)

    # Getting and printing account A random information
    account = get_account_info()
    follower_count_a = account["follower_count"]
    print("Compare A: " + format_account_info(account))

    # Printing the VS logo
    print(vs)

    # Getting and printing account B random information
    account = get_account_info()
    follower_count_b = account["follower_count"]
    print("Compare B: " + format_account_info(account))

    # Asking for an answer and making the comparison
    user_chose = input("Who has more followers? Type 'A' or 'B': ")
    account_winner = compare_followers(follower_count_a, follower_count_b)

    # Checking the result
    if user_chose.upper() == account_winner.upper():
        return True
    else:
        return False


# Starting the game
bResult = game()

print(bResult)
# Count points and show results
while bResult:
    score += 1
    clear()
    print(f"You're right! Current score: {score}")
    bResult = game()
else:
    clear()
    print(f"Sorry, that's wrong. Final score: {score}")
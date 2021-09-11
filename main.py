from art import logo, vs
from game_data import data
from random import choice
import os

clear = lambda: os.system('cls')


def formatted_account_data(account):
    """Takes the account data and returns the printable formatted string"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."


def check_the_guess(guess, a_followers, b_followers):
    """Takes the user guess and follower counts of A & B and returns 'True' if the user is correct or 'False' if the
    user is wrong """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    # Display the art
    print(logo)

    score = 0
    is_game_over = False

    # Generate a random account from game_data list
    account_a = choice(data)
    account_b = choice(data)

    # Make the game repeatable
    while not is_game_over:

        # Make some functionality to make account B as account A for next turn and account B as new account
        account_a = account_b
        account_b = choice(data)
        while account_a == account_b:
            account_b = choice(data)

        # Make the account to be in a printable format
        print(f"Compare A : {formatted_account_data(account_a)}")
        print(vs)
        print(f"Against B : {formatted_account_data(account_b)}")

        # Ask the user for a guess
        guess = input("\n Who has more followers? Type 'A' or 'B': ").lower()

        # Get the followers count of A & B
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        # Check if the user is correct based on the follower counts
        is_correct = check_the_guess(guess, a_followers, b_followers)

        # clear the screen before each turn
        clear()
        print(logo)

        # Give a feedback to the user 
        # keep track of the score
        if is_correct:
            score += 1
            print(f"You are right! Current score : {score}")
        else:
            is_game_over = True
            print(f"Sorry you are wrong! Final score : {score}")


play_game()

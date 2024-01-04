# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:25:43 2024

@author: patri
"""
import random
import time

score = {"Wins": 0, "Losses": 0, "Ties": 0, "Runs": 0}

def get_user_choice():
    while True:
        choice = input("Type 'Rock', 'Paper', 'Scissors', or 'Quit' to stop playing. You can also check the 'Board'.\n Typing just the first letter works too: ")
        if choice.upper() in ["R", "P", "S", "ROCK", "PAPER", "SCISSORS", "QUIT", "Q", "BOARD"]:
            return choice.upper()
        else:
            print("Invalid choice. Please try again.")

def display_score():
    print("\nCurrent Score:")
    for key, value in score.items():
        print(f"{key}: {value}")
    print()

def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "R" and computer == "S") or (player == "P" and computer == "R") or (player == "S" and computer == "P"):
        return "Player Wins"
    else:
        return "Computer Wins"

def play_again():
    return input("Would you like to play again? [Y or N]\n").upper() in ["Y", "YES"]

def game():
    adjectives = ["Glorious", "Magnificent", "Exuberant", "Admirable", "Amazing", "Astonishing", "Awesome", "Brilliant", "Cool", "Enjoyable", "Excellent", "Fabulous", "Fantastic", "Fine", "Incredible", "Magnificent", "Marvelous", "Outstanding", "Phenomenal", "Pleasant", "Pleasing", "Remarkable", "Sensational", "Strange", "Superb", "Surprising", "Terrific", "Tremendous", "Wondrous", "Astounding", "Awe-inspiring", "Groovy", "Grrrrrrrreat", "Great", "Miraculous", "Peachy", "Something-else", "Staggering", "Startling", "Stupendous", "Super", "Swell", "Unheard-of"]

    while True:
        p_choice = get_user_choice()
        c_choice = random.choice(["R", "P", "S"])
        adj = random.choice(adjectives)

        print(f"\nYou chose {p_choice} and the {adj} Computer chose: {c_choice}\n")

        result = determine_winner(p_choice, c_choice)

        if result == "Tie":
            print("It's a tie!\n")
            score["Ties"] += 1
        elif result == "Player Wins":
            print("You win the pot!\n")
            time.sleep(2)
            print("Notice: There is no money in the pot, sorry...\n")
            score["Wins"] += 1
        else:
            print("Computer wins!\n")
            score["Losses"] += 1

        score["Runs"] += 1

        display_score()

        if not play_again():
            print("\nFine! The Computer was tired of playing against you anyway.\n")
            time.sleep(2)
            print("Bye!")
            time.sleep(2)
            break

if __name__ == "__main__":
    game()

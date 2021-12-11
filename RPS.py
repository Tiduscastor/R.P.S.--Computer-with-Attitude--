# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:01:05 2021

@author: patrick Wesley
"""
import random
import time
import sys

score = {"Wins": 0, "Losses": 0, "Ties": 0, "Runs": 0}

def game():
    countStart = 4
    a = ["Glorious", "Magnificant", "Exhuberant", "Admirable", "Amazing", "Astonishing", "Awesome", "Brilliant", "Cool", "Enjoyable", "Excellent", "Fabulous", "Fantastic", "Fine", "Incredible", "Magnificent", "Marvelous", "Outstanding", "Phenomenal", "Pleasant", "Pleasing", "Remarkable", "Sensational", "Strange", "Superb", "Surprising", "Terrific", "Tremendous", "Wondrous", "Astounding", "Awe-inspiring", "Groovy", "Grrrrrrrreat", "Great", "Miraculous", "Peachy", "Something-else", "Staggering", "Startling", "Stupendous", "Super", "Swell", "Unheard-of"]
    i = [0, 1, 2]
    pChoice = input("Type:'Rock', 'Paper', 'Scissors', or 'Quit' to stop playing. You can also check the 'Board'.\n Typing just the first letter works too")
    
    def again():
        countAgain = 4
    
        while True:
            newgame = input("Would you like to play? [Y or N]\n")
            
            if countAgain == 0:
                break
            elif newgame.upper() != "Y" and newgame.upper() != "YES" and newgame.upper() != "N" and newgame.upper() != "NO":
                print("Type one of the given options, please.")
                print(countAgain, "Tries left to follow directions.")
                countAgain -= 1
            elif newgame.upper() == "YES" or newgame.upper() == "Y":
                print("\nGreat!")
                game()
            else:
                print("\nFine! The Computer was tired of playing against you anyway.\n")
                time.sleep(2)
                print("Bye!")
                time.sleep(2)
                break

    while True:
        cChoice = random.choice(i)
        adj = random.choice(a)
        if pChoice.upper() == "R" or pChoice.upper() == "ROCK":
            if cChoice == 0:
                x = "Rock!"
                print("\nYou chose Rock and the {} Computer chose: {}\n".format(adj, x))
                print("\nIt's a tie!\n")
                score["Ties"] = score.get("Ties", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
            elif cChoice == 1:
                x = "Paper!"
                print("\nYou chose Rock and the {} Computer chose: {}\n".format(adj, x))
                print("\nPaper covers your crumbly rock! You lose!\n")
                score["Losses"] = score.get("Losses", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
            else:
                x = "Scissors!"
                print("\nYou chose Rock and the {} Computer chose: {}\n".format(adj, x))
                print("\nYou Win the pot!\n")
                time.sleep(2)
                print("Notice: There is no money in the pot, sorry...\n")
                score["Wins"] = score.get("Wins", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
        elif pChoice.upper() == "P" or pChoice.upper() == "PAPER":
            if cChoice == 0:
                x = "Rock!"
                print("\nYou chose Paper and the {} Computer chose: {}\n".format(adj, x))
                print("\nYou Win the pot!")
                time.sleep(2)
                print("Notice: There is no money in the pot, sorry...\n")
                score["Wins"] = score.get("Wins", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
            elif cChoice == 1:
                x = "Paper!"
                print("\nYou chose Paper and the {} Computer chose: {}\n".format(adj, x))
                print("\nIt's a tie!\n")
                score["Ties"] = score.get("Ties", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
            else:
                x = "Scissors!"
                print("\nYou chose Paper and the {} Computer chose: {}\n".format(adj, x))
                print("\nScissors slash your pathetic paper to ribbons!\n")
                score["Losses"] = score.get("Losses", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
        elif pChoice.upper() == "S" or pChoice.upper() == "SCISSORS":
            if cChoice == 0:
                x = "Rock!"
                print("\nYou chose Scissors and the {} Computer chose: {}\n".format(adj, x))
                print("\nYour pathetic scissors are destroyed via rockslide.\n")
                score["Losses"] = score.get("Losses", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
            elif cChoice == 1:
                x = "Paper!"
                print("\nYou chose Scissors and the {} Computer chose: {}\n".format(adj, x))
                print("\nYou Win the pot!")
                time.sleep(2)
                print("Notice: There is no money in the pot, sorry...\n")
                score["Wins"] = score.get("Wins", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
            else:
                x = "Scissors!"
                print("\nYou chose Scissors and the {} Computer chose: {}\n".format(adj, x))
                print("\nIt's a tie!\n")
                score["Ties"] = score.get("Ties", 0) + 1
                score["Runs"] = score.get("Runs", 0) + 1
                again()
        elif pChoice.upper() == "Q" or pChoice.upper() == "QUIT":
            print("Come back again later if you want to lose to me again...")
            time.sleep(1)
            print("I mean the {} Computer\n".format(adj))
            time.sleep(3)
            print("Bye")
            time.sleep(1)
            sys.exit()
        elif pChoice.upper() == "B" or pChoice.upper() == "Board":
            for x in score:
                print(score)
                again()
        else:
            countStart = 4
            while True:
                tryAgain = input("That was not one of the possible choices... Try again? [Y or N]")
                if countStart == 0:
                    sys.exit()
                elif tryAgain.upper() != "Y" and tryAgain.upper() != "YES" and tryAgain.upper() != "N" and tryAgain.upper() != "NO":
                    print("Type one of the given options, please.")
                    print(countStart, "Tries left to follow directions.")
                    countStart -= 1
                elif tryAgain.upper() == "YES" or tryAgain.upper() == "Y":
                    print("\nFinally!")
                    game()
                else:
                    print("Alright then, bye!")
                    time.sleep(2)
                    sys.exit()

def Saw():
    countSaw = 4
    while True:
        newgame = input("Do you want to play a game? [Y or N]\n")
        if countSaw == 0:
            break
        elif newgame.upper() != "Y" and newgame.upper() != "YES" and newgame.upper() != "N" and newgame.upper() != "NO":
            print("Type one of the given options, please.")
            print(countSaw, "Tries left.")
            countSaw -= 1
        elif newgame.upper() == "YES" or newgame.upper() == "Y":
            print("\nGreat!")
            game()
        else:
            print("\nOk, then! The Computer didn't wan't to be seen playing with you anyway.\n")
            time.sleep(2)
            print("Bye!")
            time.sleep(2)
            break

Saw()
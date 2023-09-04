
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerschoice = input("Enter... \n1 Rock, \n2 Paper, \n3 Scissors\n\n ")

player = int(playerschoice)

if player < 1 or player > 3:
    sys.exit("You have to pick a number between 1 and 3!\n\n")
computerchoice = random.choice([1, 3])  # List of choices

print("Your choice: " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose: " + str(RPS(computerchoice)).replace('RPS.', '') + ".")

if player == 1 and computerchoice == 3:
    print("You win!!! 😊")
elif player == 2 and computerchoice == 1:
    print("You win!!! 😊")
elif player == 3 and computerchoice == 2:
    print("You win!!! 😊")
elif player == computerchoice:
    print("You tie!!! 😮")
else:
    print("You Lose!! 🐍3")

print("")
print("")
print("")

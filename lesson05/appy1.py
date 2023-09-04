import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerschoice = input("Enter... \n1 Rock, \n2 Paper, \n3 Sissors\n\n ")


player = int(playerschoice)

if player < 1 or player > 3:
    sys.exit("You have to pick a number between 1 and 3!\n\n")

computerchoice = random.choice("1, 3")

computer = int(computerchoice)

print("Your choice : " + str(RPS(player)) + "" ".")
print("Python chose: " + str(RPS(computer)) + "" ".")

if player == 1 and computer == 3:
    print("You win!!!  😊 ")
elif player == 2 and computer == 1:
    print("You win!!!  😊 ")
elif player == 3 and computer == 2:
    print("You win!!!  😊 ")
elif player == computer:
    print("You tie!!!  😮 ")
else:
    print("You Lose!! 🐍3")

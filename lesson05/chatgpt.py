import sys
import random

print("")
playerschoice = input("Enter... \n1 Rock, \n2 Paper, \n3 Scissors\n\n ")

player = int(playerschoice)

if player < 1 or player > 3:
    sys.exit("You have to pick a number between 1 and 3!\n\n")

computerchoice = random.randint(1, 3)

print("Your choice: " + str(player) + ".")
print("Python chose: " + str(computerchoice) + ".")

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

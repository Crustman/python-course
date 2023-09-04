
import sys
import random
from enum import Enum

print("")
print("*******************************************")
print("")


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerschoice = input(
        "Enter... \n1 Rock, \n2 Paper, \n3 Scissors\n\n ")

    if playerschoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3, ")
        return play_rps()

    player = int(playerschoice)

    computerchoice = random.choice([1, 3])  # List of choices

    computer = int(computerchoice)

    print("Your choice: " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose: " + str(RPS(computerchoice)).replace('RPS.', '') + ".")

    def decide_winner(player, computer):
        if player == 1 and computerchoice == 3:
            return "You win!!! 😊"
        elif player == 2 and computerchoice == 1:
            return "You win!!! 😊"
        elif player == 3 and computerchoice == 2:
            return "You win!!! 😊"
        elif player == computerchoice:
            return "You tie!!! 😮"
        else:
            return "You Lose!! 🐍3"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("Game count: " + str(game_count))

    print("\nPlay again?? ")
    while True:
        playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n👌")
        print("Thank you for playing!\n")
        playagain = False
        sys.exit("Bye! 👋")


play_rps()


print("")
print("")
print("")
print("")
print("")
print("*********************************************")
print("")
print("")

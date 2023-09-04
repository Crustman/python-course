import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def decide_winner(player, computer):
    if player == 1 and computer == 3:
        return "You win!!! 😊"
    elif player == 2 and computer == 1:
        return "You win!!! 😊"
    elif player == 3 and computer == 2:
        return "You win!!! 😊"
    elif player == computer:
        return "You tie!!! 😮"
    else:
        return "You Lose!! 🐍3"


def play_rps():
    print("\n*******************************************\n")

    playerschoice = input("Enter...\n1 Rock,\n2 Paper,\n3 Scissors\n\n ")

    if playerschoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerschoice)
    computer = random.choice([1, 3])  # List of choices

    print("Your choice:", RPS(player).name)
    print("Python chose:", RPS(computer).name)

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("Game count:", game_count)

    print("\nPlay again?")
    while True:
        playagain = input("\nPlay again?\nY for Yes or\nQ to Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n👌")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


if __name__ == "__main__":
    game_count = 0
    play_rps()

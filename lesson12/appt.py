
import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computerchoice == 3:
                player_wins += 1
                return "You win!!! 😊"
            elif player == 2 and computerchoice == 1:
                player_wins += 1
                return "You win!!! 😊"
            elif player == 3 and computerchoice == 2:
                player_wins += 1
                return "You win!!! 😊"
            elif player == computerchoice:
                return "You tie!!! 😮"
            else:
                python_wins += 1
                return "You Lose!! 🐍3"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

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
            sys.exit("Bye! 👋")

    return play_rps


play = rps()

play()

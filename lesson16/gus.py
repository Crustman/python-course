import sys
import random


def play_number_game():
    global name
    global player_wins
    
    playerchoice = input(f"\n{name}, try and guess a number I'm 1, 2, 3: \n")
    if playerchoice not in [1, 2, 3]:
        print(f"{name}, please enter a number 1, 2, 3")
        return play_number_game()
    
    computer_choice = random.choice (1,2,3)
    
    print(f"\n{name} chose "  {computer_choice}.")
          
          
          
    
    
    
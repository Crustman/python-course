import random

def horse_track():
    print("Welcome to Horse Track!")
    horses = ["Thunderbolt", "Midnight Star", "Golden Arrow", "Silver Streak", "Swift Runner"]
    odds = [3, 4, 5, 6, 7]
    
    player_balance = 100
    while player_balance > 0:
        print("\nAvailable Horses:")
        for i, horse in enumerate(horses):
            print(f"{i + 1}. {horse} (Odds: {odds[i]}x)")
        
        player_bet = 0
        while player_bet <= 0 or player_bet > player_balance:
            player_bet = int(input("\nPlace your bet (0 to quit): "))
            if player_bet == 0:
                return
            
            selected_horse = int(input("Choose a horse (1-5): ")) - 1
            if selected_horse < 0 or selected_horse >= len(horses):
                print("Invalid horse selection. Try again.")
                continue
            
            winning_horse = random.choices(horses, weights=odds, k=1)[0]
            print(f"The race is over! {winning_horse} wins!")
            
            if selected_horse == horses.index(winning_horse):
                winnings = player_bet * odds[selected_horse]
                player_balance += winnings
                print(f"Congratulations! You won {winnings} coins!")
            else:
                player_balance -= player_bet
                print("Sorry, you lost your bet.")
            
            print(f"Your balance: {player_balance} coins")
    
    print("Game over! You've run out of coins.")

if __name__ == "__main__":
    horse_track()



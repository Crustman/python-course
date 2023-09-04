print('\n')


def parent_funtion(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins lfet.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins lfet.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


tommy = parent_funtion("Tommy", 3)
jenny = parent_funtion("Jenny", 5)

tommy()
tommy()
tommy()

jenny()


print("\n")

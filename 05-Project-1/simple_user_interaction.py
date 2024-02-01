                    # Simple User Interaction

game_list = [0, 1, 2]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

display_game(game_list)

def position_choice():
    choice = "wrong"

    while choice not in ["0", "1", "2"]:
        choice = input("Pick a position (0, 1, 2): ")

        if choice not in ["0", "1", "2"]:
            print("Sorry, invalid choice!")

    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list

def gameon_choice():
    choice = "wrong"

    while choice not in ["Y", "N"]:
        choice = input("Keep playing? (Y or N): ")

        if choice not in ["Y", "N"]:
            print("Sorry, I don't understand, please choose Y or N")

    if choice == "Y":
        return True
    else:
        return False

# Variable to keep game playing
game_on = True

# First Game List
game_list = [0, 1, 2]

while game_on:
    # Clear any historical output and show the game list
    display_game(game_list)

    # Have player choose position
    position = position_choice()

    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list, position)

    # Clear Screen and show the updated game list
    display_game(game_list)

    # Ask if you want to keep playing
    game_on = gameon_choice()

                        # Final Code
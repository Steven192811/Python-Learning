from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] + "|" + board[8] + "|" + board[9]) # 7|8|9
    print("-|-|-")
    print(board[4] + "|" + board[5] + "|" + board[6]) # 4|5|6
    print("-|-|-")
    print(board[1] + "|" + board[2] + "|" + board[3]) # 1|2|3


def player_input():
    marker = "" # initialize marker
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O: ").upper() # ask player 1 to choose X or O

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker # place marker at position on board


def win_check(board, mark): # check if mark has won
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the left
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal


import random


def choose_first():

    flip = random.randint(0, 1) # generate random number between 0 and 1

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
        # Board is full if we return True
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose a position: (1-9) "))
    return position


def replay():
    choice = input("Play again? Enter Yes or No")
    return choice == "Yes"

# WHILE LOOP TO KEEP RUNNING THE GAME

print("Welcome to Tic Tac Toe")

while True:

    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHO'S FIRST, CHOOSE MARKERS X, O)

    the_board = [" "] * 10 # create a list to represent the board

    player1_marker, player2_marker = player_input() # assign player 1 and player 2 markers

    turn = choose_first() # randomly choose who goes first
    print("The " + turn + " will go first")

    play_game = input("Ready to play? y or n? ")

    if play_game == "y":
        game_on = True
    else:
        game_on = False
    # Game play

    while game_on:

        if turn == "Player 1":
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)
            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = "Player 2"

    if not replay():
        break

# Break out of the while loop on replay() if not True

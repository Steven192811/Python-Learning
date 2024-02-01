from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-|-|-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-|-|-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O: ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the left
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal



import random

WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)]             # diagonals


def show(board):
    for row in (0, 3, 6):
        print(" | ".join(board[row:row + 3]))
    print()


def wins(board, s):
    return any(board[a] == board[b] == board[c] == s for a, b, c in WINS)


def ai_move(board):
    free = [i for i, c in enumerate(board) if c.isdigit()]
    for s in "OX":  # first try to win (O), then block the player (X)
        for i in free:
            if wins(board[:i] + [s] + board[i + 1:], s):
                return i
    return random.choice(free)


board = list("123456789")  # empty cells show their number
turn = "X"                 # you are X, the AI is O

while True:
    show(board)
    if turn == "X":
        move = input("Your move (1-9): ")
        if not move.isdigit() or move not in board:
            print("Invalid move.")
            continue
        i = board.index(move)
    else:
        i = ai_move(board)

    board[i] = turn
    if wins(board, turn):
        show(board)
        print("You win!" if turn == "X" else "AI wins!")
        break
    if not any(c.isdigit() for c in board):
        show(board)
        print("It's a tie!")
        break
    turn = "O" if turn == "X" else "X"

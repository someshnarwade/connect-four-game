"""
Connect4 Game Tutorial
by Keith Galli
Youtube Channel: https://www.youtube.com/channel/UCq6XkhO5SZ66N04IcPbqNcw
Video URL: https://www.youtube.com/watch?v=zD-Xuu_Jpe4
Part 2: Check for winning move
"""
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board_init = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board_init


def drop_piece(given_board, given_row, given_column, given_piece):
    given_board[given_row][given_column] = given_piece


def is_valid_location(given_board, given_column):
    return given_board[ROW_COUNT - 1][given_column] == 0


def get_next_open_row(given_board, given_column):
    for r in range(ROW_COUNT):
        if given_board[r][given_column] == 0:
            return r


def print_board(given_board):
    print(np.flip(given_board, 0))


def winning_move(given_board, given_piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if all([given_board[r][c+i] == given_piece for i in range(4)]):
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all([given_board[r+i][c] == given_piece for i in range(4)]):
                return True
    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all([given_board[r+i][c+i] == given_piece for i in range(4)]):
                return True
    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all([given_board[r-i][c+i] == given_piece for i in range(4)]):
                return True
    return False


board = create_board()
game_over = False
turn = True
p1_piece = 1
p2_piece = 2

while not game_over:
    print_board(board)
    # Ask for player input
    if turn:
        column = int(input("Player One, Make Your Selection (0-6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, p1_piece)
            if winning_move(board, p1_piece):
                print("Player One Wins!")
                game_over = True
            turn = False
    else:
        column = int(input("Player Two, Make Your Selection (0-6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, p2_piece)
            if winning_move(board, p2_piece):
                print("Player Two Wins!")
                game_over = True
            turn = True

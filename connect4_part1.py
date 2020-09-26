"""
Connect4 Game Tutorial
by Keith Galli
Youtube Channel: https://www.youtube.com/channel/UCq6XkhO5SZ66N04IcPbqNcw
Video URL: https://www.youtube.com/watch?v=UYgyRArKDEs
Part 1: Basic Structure and Game Loop
"""
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board_init = np.zeros((6, 7))
    return board_init


def drop_piece(given_board, given_row, given_column, given_piece):
    given_board[given_row][given_column] = given_piece


def is_valid_location(given_board, given_column):
    return given_board[5][given_column] == 0


def get_next_open_row(given_board, given_column):
    for r in range(ROW_COUNT):
        if given_board[r][given_column] == 0:
            return r


def print_board(given_board):
    print(np.flip(given_board, 0))


board = create_board()
print_board(board)
game_over = False
turn = True
p1_piece = 1
p2_piece = 2

while not game_over:
    # Ask for player input
    if turn:
        column = int(input("Player One, Make Your Selection (0-6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, p1_piece)
        turn = False
    else:
        column = int(input("Player Two, Make Your Selection (0-6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, p2_piece)
        turn = True

    print_board(board)

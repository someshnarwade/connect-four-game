"""
Connect4 Game Tutorial
by Keith Galli
Youtube Channel: https://www.youtube.com/channel/UCq6XkhO5SZ66N04IcPbqNcw
Video URL: https://youtu.be/krCKxcrHeN4
Part 4: Game Animation & Additional Features
"""
import sys

import numpy as np
import pygame

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


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
            if all([given_board[r][c + i] == given_piece for i in range(4)]):
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all([given_board[r + i][c] == given_piece for i in range(4)]):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all([given_board[r + i][c + i] == given_piece for i in range(4)]):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all([given_board[r - i][c + i] == given_piece for i in range(4)]):
                return True
    return False


def draw_board(given_board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(
                screen,
                BLUE,
                (
                    c * SQUARE_SIZE,
                    r * SQUARE_SIZE + SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                ),
            )
            pygame.draw.circle(
                screen,
                BLACK,
                (c * SQUARE_SIZE + RADIUS, r * SQUARE_SIZE + SQUARE_SIZE + RADIUS),
                RADIUS - 5,
            )
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if given_board[r][c] == 1:
                pygame.draw.circle(
                    screen,
                    RED,
                    (c * SQUARE_SIZE + RADIUS, height - (r * SQUARE_SIZE + RADIUS)),
                    RADIUS - 5,
                )
            elif given_board[r][c] == 2:
                pygame.draw.circle(
                    screen,
                    YELLOW,
                    (c * SQUARE_SIZE + RADIUS, height - (r * SQUARE_SIZE + RADIUS)),
                    RADIUS - 5,
                )
    pygame.display.update()


board = create_board()
game_over = False
turn = True
p1_piece = 1
p2_piece = 2

pygame.init()

SQUARE_SIZE = 100

width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)
RADIUS = int(SQUARE_SIZE / 2)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 70)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            posx = event.pos[0]
            if turn:
                pygame.draw.circle(screen, RED, (posx, RADIUS), RADIUS - 5)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, RADIUS), RADIUS - 5)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            # Ask for player input
            posx = event.pos[0]
            column = posx // SQUARE_SIZE

            if turn:
                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, p1_piece)
                    if winning_move(board, p1_piece):
                        label = myfont.render("Player One Wins!", 1, RED)
                        screen.blit(label, (20, 10))
                        game_over = True
                    turn = False
            else:
                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, p2_piece)
                    if winning_move(board, p2_piece):
                        label = myfont.render("Player Two Wins!", 1, YELLOW)
                        screen.blit(label, (20, 10))
                        game_over = True
                    turn = True

            draw_board(board)

            if game_over:
                pygame.time.wait(3000)

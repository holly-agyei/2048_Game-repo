import tkinter as tk
import random

# Initialize the board
def init_board():
    return [[0, 0, 0, 0] for _ in range(4)]

# Add a random tile (2 or 4) to an empty cell
def add_random(board):
    empty = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = random.choice([2, 4])

# Compress the row to shift all non-zero tiles to the left
def compress(row):
    new_row = [x for x in row if x != 0]
    new_row += [0] * (4 - len(new_row))
    for i in range(4):
        row[i] = new_row[i]
# Merge adjacent tiles with the same value
def merge(row):
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0

# Move tiles left
# Merge adjacent tiles with the same value
def merge(row):
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0

# Move tiles left
def move_left(board):
    for r in range(4):
        compress(board[r])
        merge(board[r])
        compress(board[r])
def move_right(board):
    for r in range(4):
        row = board[r][::-1]
        compress(row)
        merge(row)
        compress(row)
        board[r] = row[::-1]

# Move tiles up
def move_up(board):
    for c in range(4):
        column = [board[r][c] for r in range(4)]
        compress(column)
        merge(column)
        compress(column)
        for r in range(4):
            board[r][c] = column[r]



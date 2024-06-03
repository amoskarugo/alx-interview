#!/usr/bin/python3
import sys

args = sys.argv


def validate(commands) -> None:
    if len(commands) < 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(commands[1])

    except Exception as e:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    return None


validate(args)
cells = int(int(args[1]))
chessBoard = []
for i in range(cells):
    row = []
    for j in range(cells):
        row.append(False)
    chessBoard.append(row)


def display(board):
    positions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                positions.append([i, j])
    print(positions)


def isSafe(board, r, c):
    # check if it is safe to place the queen vertically
    for i in range(r):
        if board[i][c]:
            return False
    # check diagonal left
    max_left = min(r, c)
    for j in range(1, max_left + 1):
        if board[r - j][c - j]:
            return False
    # check diagonal right
    max_right = min(r, len(board) - c - 1)
    for k in range(1, max_right + 1):
        if board[r - k][c + k]:
            return False
    return True


def queens(board, row_):
    if len(board) == row_:
        display(board)
        return 1

    count = 0
    for col in range(len(board)):
        if isSafe(board, row_, col):
            board[row_][col] = True
            count = count + queens(board, row_ + 1)
            board[row_][col] = False
    return count


queens(chessBoard, 0)

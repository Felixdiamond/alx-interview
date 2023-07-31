#!/usr/bin/python3
"""N Queens problem"""
import sys


def isSafe(board, row, col, n):
    """Check if a queen can be placed on board"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col, n):
    """Solve the n queen problem"""
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return True
    res = False
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1, n) or res
            board[i][col] = 0
    return res


def solveNQ(n):
    """Solve the N Queen problem"""
    board = [[0 for j in range(n)] for i in range(n)]
    if not solveNQUtil(board, 0, n):
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solveNQ(n)


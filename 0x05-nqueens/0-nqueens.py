#!/usr/bin/python3
""" N queens puzzle solution : """

from sys import argv


def is_NQueen(cell: list) -> bool:
    """True if N Queen False otherwise"""
    row_number = len(cell) - 1
    difference = 0
    for index in range(0, row_number):
        difference = cell[index] - cell[row_number]
        if difference < 0:
            difference *= -1
        if difference == 0 or difference == row_number - index:
            return False
    return True


def solve_NQueens(dimension: int, row: int, cell: list, output: list):
    """A method that returns result of N Queens recursively"""
    if row == dimension:
        print(output)
    else:
        for column in range(0, dimension):
            cell.append(column)
            output.append([row, column])
            if (is_NQueen(cell)):
                solve_NQueens(dimension, row + 1, cell, output)
            cell.pop()
            output.pop()


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    N = int(argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if N < 4:
    print('N must be at least 4')
    exit(1)
else:
    output = []
    cell = 0
    solve_NQueens(int(N), cell, [], output)

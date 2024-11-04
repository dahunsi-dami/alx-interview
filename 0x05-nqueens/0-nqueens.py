#!/usr/bin/python3
"""N Queens Puzzle challenge solution."""

import sys


def print_usage_and_exit(message):
    """Prints an error message & exists w/ status 1."""
    print(message)
    sys.exit(1)


def is_valid_position(queens, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(N, row, queens, solutions):
    """
    Recursively places queens on board and-
    -saves each solution.
    """
    if row == N:
        solutions.append([[r, c] for r, c in queens])
        return

    for col in range(N):
        if is_valid_position(queens, row, col):
            queens.append((row, col))
            solve_nqueens(N, row + 1, queens, solutions)
            queens.pop()


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = []
    solve_nqueens(N, 0, [], solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

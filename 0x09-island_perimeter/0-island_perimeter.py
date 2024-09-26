#!/usr/bin/python3
"""Module to calculate island perimeter."""


def island_perimeter(grid):
    """Returns perimeter of island in grid."""
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][column] == 1:
                    perimeter -= 2
                if column > 0 and grid[row][column - 1] == 1:
                    perimeter -= 2

    return perimeter

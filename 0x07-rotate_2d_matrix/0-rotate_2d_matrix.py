#!/usr/bin/python3
"""2D Matrix 90 degree clockwise implementation."""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise."""
    rows = len(matrix)

    for i in range(rows):
        for j in range(i, rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(rows):
        matrix[i].reverse()

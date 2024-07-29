#!/usr/bin/python3
"""
Module provides a function that generates
Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Function generates Pascal's Triangle up to n rows.

    Args:
        n (int): number of rows to generate.

    Returns:
        a list of list of integers. Each list in list is a row.
    """

    if n <= 0:
        return []

    # Establish state of triangle as list of lists
    triangle = [[1]]

    # Use a single loop for complexity sake
    for i in range(1, n):
        backrow = triangle[i - 1]

        # Set 1st element of current row to 1 always
        row = [1]

        # Fill in values in 'row' with list comprehension
        row.extend(
            [backrow[j] + backrow[j + 1] for j in range(len(backrow) - 1)]
        )

        # End 'row' with 1 always
        row.append(1)

        # Join the new row to base of the triangle
        triangle.append(row)

    return triangle

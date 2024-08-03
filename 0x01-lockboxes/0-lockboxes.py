#!/usr/bin/python3
"""Module with method to tell if all boxes can be opened."""


def canUnlockAll(boxes):
    """Method to determine if all boxes can be opened."""

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        box_num = stack.pop()
        for i in boxes[box_num]:
            if 0 <= i < n and not unlocked[i]:
                unlocked[i] = True
                stack.append(i)

    return all(unlocked)

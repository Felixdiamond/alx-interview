#!/usr/bin/python3
"""This module defines a function canUnlockAll that takes a list of lists representing boxes and determines if all the boxes can be opened."""

from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    This function takes a list of lists, where each inner list represents a box and contains the keys to other boxes.
    The function returns True if all boxes can be opened, and False otherwise.

    Args:
        boxes: A list of lists, where each inner list represents a box and contains the keys to other boxes.

    Returns:
        A boolean value indicating whether all boxes can be opened or not.
    """
    keys = [0]
    opened = [False] * len(boxes)
    opened[0] = True
    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                keys.append(key)
    return all(opened)

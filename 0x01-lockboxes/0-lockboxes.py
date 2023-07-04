#!/usr/bin/python3
"""Module containing the canUnlockAll function"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists, where each inner list represents a box and contains the keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
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

#!/usr/bin/python3
"""
Module to calculate the perimeter of an island
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    width = len(grid[0])
    height = len(grid)
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if i == height - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == width - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter


#!/usr/bin/python3
"""Function island_perimeter calculates the perimeter of
an island represented in a grid using a straightforward approach.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    pr = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    pr += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    pr += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    pr += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    pr += 1
    return pr

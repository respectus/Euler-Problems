"""
Path Sum: Three Ways
Project Euler Problem #82
by Muaz Siddiqui

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left 
column and finishing in any cell in the right column, and only moving up, down, 
and right, is indicated in red and bold; the sum is equal to 994.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right 
by only moving right and down.
"""
from euler_helpers import timeit

@timeit
def answer():
    f = open('p081_matrix.txt', 'r')
    data = [list(map(int,row.split(','))) for row in f.read().split()]
    """
    This time it's similar to flipping the table to its side and searching from top
    to bottom, but there are multiple starting points, namely the first element of
    each row. We calculate the min paths from the starting cell of each row and then
    take the minimum of those min paths.
    """
    min_path = [data[n][79] for n in range(80)]
    for y in range(78,-1, -1):
        min_path[0] += data[0][y]
        # Sweep up and right
        for x in range(1,80):
            min_path[x] = min(min_path[x], min_path[x-1]) + data[x][y]
        # Sweep down as well and if it is better than the previously found path
        # then use that instead.
        for x in range(78,-1,-1):
            min_path[x] = min(min_path[x], min_path[x+1] + data[x][y])
    return min(min_path)
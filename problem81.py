"""
Path Sum: Two Ways
Project Euler Problem #81
by Muaz Siddiqui

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom 
right, by only moving to the right and down, is indicated in bold red and is equal 
to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right 
by only moving right and down.
"""
from euler_helpers import timeit

@timeit
def answer():
    f = open('p081_matrix.txt', 'r')
    data = [list(map(int,row.split(','))) for row in f.read().split()]
    for x in range(80):
        for y in range(80):
            data[x][y] += min(data[x][y-1], data[x-1][y]) if x>0 and y>0 else (data[x-1][y] if x else (data[x][y-1] if y else 0))
    return data[-1][-1]
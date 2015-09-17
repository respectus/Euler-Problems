"""
Number Spiral Diagonals
Project Euler Problem #28
by Muaz Siddiqui

Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
"""

# No brute forcing, just simple observations :)
# The diagonals contain for an n-spiral contain all the odd squares up to n
# and they contain the diag = even squares + 1 along with diag +- even

def spiral_diagonals(n):
    diag_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            diag_sum += i ** 2
        else:
            odd_square = (i ** 2) + 1
            diag_sum += odd_square + (odd_square + i) + (odd_square - i)
    return diag_sum

def answer():
    return spiral_diagonals(1001)
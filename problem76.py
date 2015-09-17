"""
Counting Summations
Project Euler Problem #76
by Muaz Siddiqui

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two 
positive integers?
"""
from euler_helpers import timeit

@timeit
def answer():
    # Similar to the coin sums problem but we change the coin values
    # adds all the previous ways to the newest perm(b)
    goal = 100
    perms = [1] + [0] * goal
    for a in range(1, goal):
        for b in range(a, goal + 1):
            perms[b] += perms[b - a]
    return perms[goal]


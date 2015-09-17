"""
Cubic Permutations
Project Euler Problem #62
by Muaz Siddiqui

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 
(3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has 
exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
from euler_helpers import timeit
import itertools, collections

@timeit
def answer():
    # Atleast five permutations so we start at 3 digits
    cubes = collections.defaultdict(list)
    count = 5
    while True:
        c = cubes[''.join(sorted(str(count ** 3)))]
        c.append(count)
        count += 1
        if len(c) == 5:
            return min(c) ** 3
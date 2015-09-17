"""
Cubic Permutations
Project Euler Problem #63
by Muaz Siddiqui

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 
134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from euler_helpers import timeit
import itertools, math
@timeit
def answer():
    count = 0
    done = False
    nums = {}
    n = 1
    while not done:
        lowest = int(math.ceil(10**((n-1)/n)))
        if lowest >= 10:
            done = True
        count += 10 - lowest
        nums[n] = [num**n for num in range(lowest, 10)]
        n += 1
    print(nums)
    return count
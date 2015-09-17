"""
Coin Partitions
Project Euler Problem #78
by Muaz Siddiqui

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five 
thousand different ways?
"""
from euler_helpers import timeit

@timeit
def answer():
    # Generating Integer Partitions with pentagonal numbers
    pentagonals = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 200)], [])
    # Sign flip flops every two terms
    sign = [1,1,-1,-1]
    limit = 1000000
    partition = [1]
    index = 0
    while True:
        index += 1
        last, i = 0, 0
        while pentagonals[i] <= index:
            last += partition[int(index - pentagonals[i])] * sign[i % 4]
            i += 1
        partition.append(last % limit)
        if partition[index] == 0:
            return index
"""
Prime Summations
Project Euler Problem #77
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
from euler_helpers import timeit, sieve

@timeit
def answer():
    found = 2
    primes = sieve(100)
    while found:
        perms = [1] + [0] * found
        for a in range(len(primes)):
            for b in range(primes[a], found + 1):
                perms[b] += perms[b - primes[a]]
        if perms[found] > 5000:
            return found
        found += 1

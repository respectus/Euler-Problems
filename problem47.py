"""
Distinct primes factors
Project Euler Problem #47
by Muaz Siddiqui

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?
"""
from euler_helpers import timeit, prime_factors

def num_distinct_primes(n):
    primefac = prime_factors(n)
    count = 0
    while len(primefac) > 0:
        count += 1
        primefac = [value for value in primefac if value != primefac[0]]
    return count

@timeit
def answer():
    first = 648
    found = False
    while not found:
        if num_distinct_primes(first) != 4:
            first += 1
            continue
        elif num_distinct_primes(first + 1) != 4:
            first += 2
            continue
        elif num_distinct_primes(first + 2) != 4:
            first += 3
            continue
        elif num_distinct_primes(first + 3) != 4:
            first += 4
            continue
        else:
            found = True
    return first


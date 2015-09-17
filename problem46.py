"""
Goldbach's other conjecture
Project Euler Problem #46
by Muaz Siddiqui

It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime 
and twice a square?
"""
from euler_helpers import timeit, is_prime

def is_twiceSquare(n):
    test = (n/2) ** 0.5
    return test == int(test)

@timeit
def answer():
    smallest = 1
    proven = False
    primes = [2]

    while not proven:
        smallest += 2
        if is_prime(smallest):
            primes.append(smallest)
            continue
        proven = True
        for prime in primes:
            if is_twiceSquare(smallest - prime):
                proven = False
                break
    return smallest


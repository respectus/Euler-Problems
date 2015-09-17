"""
Prime Power Triples
Project Euler Problem #87
by Muaz Siddiqui

The smallest number expressible as the sum of a prime square, prime cube, and prime 
fourth power is 28. In fact, there are exactly four numbers below fifty that can be 
expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square,
prime cube, and prime fourth power?
"""
from euler_helpers import timeit, sieve
# Go up to sqrt of 5000000 ~ 7071
@timeit
def answer():
    count = set()
    primes = sieve(7071)
    for a in primes:
        for b in primes:
            d = a**4 + b**3
            if d >= 50000000:
                break
            for c in primes:
                e = c*c + d
                if e >= 50000000:
                    break
                count.add(e)
    return len(count)

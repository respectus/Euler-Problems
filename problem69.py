"""
Totient Maximum
Project Euler Problem #69
by Muaz Siddiqui

Euler's Totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime 
to nine, φ(9)=6.

n   Relatively Prime    φ(n)    n/φ(n)
2   1   1   2
3   1,2 2   1.5
4   1,3 2   2
5   1,2,3,4 4   1.25
6   1,5 2   3
7   1,2,3,4,5,6 6   1.1666...
8   1,3,5,7 4   2
9   1,2,4,5,7,8 6   1.5
10  1,3,7,9 4   2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""
from euler_helpers import timeit, prime_factors, primes_to

@timeit
def answer():
    #ratios = []
    # for n in range(2, 10000000):
    #     # Euler's Product Formula
    #     primes = list(set(prime_factors(n)))
    #     product = 1
    #     for p in primes: 
    #         product *= (1 - (1/p))
    #     ratios.append(1/product)
    # return ratios.index(max(ratios)) + 2
    """
    Above code runs in 66 seconds so I reanalyzed it to see how to simplify it
    We are  essentially trying to maximize distinct primes to maximize the ratio, 
    so we should just multiply primes until we reach 1,000,000 
    """
    primes = primes_to(20)
    product = 1
    n = 0
    while product * primes[n] <= 1000000:
        product *= primes[n]
        n += 1
    return product 
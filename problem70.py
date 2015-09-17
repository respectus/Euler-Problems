"""
Totient Permutation
Project Euler Problem #70
by Muaz Siddiqui

Euler's Totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of positive numbers less than or equal to n which are 
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine 
and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so 
φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 
79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the 
ratio n/φ(n) produces a minimum.
"""
from euler_helpers import timeit, prime_factors, is_perm, primes_to

@timeit
def answer():
    # ratios = []
    # for n in range(2, 10000000):
    #     # Euler's Product Formula
    #     primes = list(set(prime_factors(n)))
    #     product = 1
    #     for p in primes: 
    #         product *= (1 - (1/p))
    #     if is_perm(n, product*n):
    #         ratios.append(1/product)
    # return ratios.index(min(ratios)) + 2
    """
    The above solution would work, but it takes far longer than the minute required
    so the best is to analyze the code. It seems to minimize the ratio 1/product
    we should maximize the product and take advantage of the fact that it is the
    product of two large distinct primes close to the sqrt(10**7)
    """
    ratios = {}
    primes = primes_to(3800,2200)
    for a in range(len(primes)):
        for b in range(a+1, len(primes)):
            n = primes[a] * primes[b]
            if n < 10000000:
                phi = (primes[a] - 1) * (primes[b] - 1)
                ratio = n/phi
                if is_perm(n, phi):
                    ratios[ratio] = n
    return ratios[min(ratios.keys())]
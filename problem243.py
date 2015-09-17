"""
Resilience
Project Euler Problem #243
by Muaz Siddiqui

A positive fraction whose numerator is less than its denominator is called a proper 
fraction. For any denominator, d, there will be d−1 proper fractions; for example, 
with d = 12: 1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 
11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio 
of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""
from euler_helpers import timeit, sieve
import itertools
"""
Resilience R(d) can be thought of as the amount of numbers coprime to d divided
by d-1. This can be calculated with Euler's totient function. Therefore
R(d) = phi(d)/(d-1). All primes have an R(d) of 1 so to minimize this ratio we have
to find a highly composite number which is the product of consecutive primes and
the composites below it.
"""
@timeit
def answer():
    primes = sieve(32)
    d, x = 1, 1
    for prime in primes:
        d *= prime
        x *= prime - 1
        for n in range(2, prime):
            if x*n/(d*n - 1) < 15499/94744:
                return d*n

"""
Ordered Fractions
Project Euler Problem #71
by Muaz Siddiqui

Consider the fraction, n/d, where n and d are positive integers. If n<d and 
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of 
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order 
of size, find the numerator of the fraction immediately to the left of 3/7.
"""
from euler_helpers import timeit
from fractions import Fraction
""" We could brute-force this, but that would probably take awhile
instead some analysis can help. The most precise fraction would have a denominator 
of close to 1000000. """
@timeit
def answer():
    n = 3/7
    # Take the first 7 sig-figs and subtract 1 from the last one
    numerator = int(str(n)[2:8] + str(int(str(n)[8]) - 1))
    # Divide that by 10,000,000 and limit denominator to 1,000,000
    ratio = Fraction(numerator/10000000).limit_denominator(1000000)
    # Extract numerator
    return str(ratio).split('/')[0]
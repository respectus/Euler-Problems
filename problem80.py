"""
Square Root Digital Expansion
Project Euler Problem #80
by Muaz Siddiqui

It is well known that if the square root of a natural number is not an integer, 
then it is irrational. The decimal expansion of such square roots is infinite 
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the 
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of 
the first one hundred decimal digits for all the irrational square roots.
"""
from euler_helpers import timeit
from decimal import *
from math import sqrt

@timeit
def answer():
    getcontext().prec = 102
    sum_ = 0
    for n in range(1,101):
        next = sum(map(int,list(str(int(Decimal(n).sqrt()*10**99)))))
        if next >= 10: sum_ += next
    return sum_ 
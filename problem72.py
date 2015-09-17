"""
Counting Fractions
Project Euler Problem #72
by Muaz Siddiqui

Consider the fraction, n/d, where n and d are positive integers. If n<d and 
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of 
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for 
d ≤ 1,000,000?
"""
from euler_helpers import timeit, totient
@timeit
def answer():
    """ Use the Farey sequence of order n where the sequence lists all reduced 
    proper fractions where denominators are <= n. Length of the set is given by
    relating Fn to Euler's Totient function phi"""
    sum_ = 1
    for n in range(1,1000001):
        sum_ += totient(n)
    # subtract 2 since this formula includes 0/1 and 1/1 which we do not need
    return sum_ - 2
    
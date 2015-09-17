"""
Powerful Digit Sum
Project Euler Problem #56
by Muaz Siddiqui

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 
is almost unimaginably large: one followed by two-hundred zeros. Despite their size,
 the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum 
digital sum?
"""
from euler_helpers import timeit, digital_sum

#brute force
@timeit
def answer():
    max_ = 0
    for a in range(2, 101):
        for b in range(2, 101):
            next = digital_sum(pow(a, b))
            if next > max_:
                max_ = next
    return max_
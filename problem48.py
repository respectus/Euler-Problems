"""
Self Powers
Project Euler Problem #48
by Muaz Siddiqui

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
from euler_helpers import timeit

@timeit
def answer():
    sum_ = 0
    for i in range(1,1001):
        sum_ += (i ** i)
    return str(sum_)[-10:]
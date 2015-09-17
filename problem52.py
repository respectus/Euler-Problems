"""
Permuted Multiples
Project Euler Problem #52
by Muaz Siddiqui

It can be seen that the number, 125874, and its double, 251748, contain exactly 
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain 
the same digits.
"""
from euler_helpers import timeit, is_perm

@timeit
def answer():
    x = 100
    while True:
        if is_perm(x, 2*x) and is_perm(x, 3*x) and is_perm(x, 4*x) and is_perm(x, 5*x) and is_perm(x, 6*x):
            return x
        x += 1
"""
Double-base Palindromes
Project Euler Problem #36
by Muaz Siddiqui

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
    leading zeros.)
"""
from euler_helpers import timeit

@timeit
def answer():
    sum_all = 0
    for x in range(1,1000000,2):
        base10 = str(x)
        base2 = str(bin(x))[2:]
        if base10 == base10[::-1] and base2 == base2[::-1]:
            sum_all += x
    return sum_all
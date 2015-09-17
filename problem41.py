"""
Pandigital Prime
Project Euler Problem #41
by Muaz Siddiqui

We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from euler_helpers import timeit, perms, is_prime

# The largest prime pandigital should start from 9 then go down
# I found it in the 7-digit range
@timeit
def answer():
    pandigitals = perms(7654321)
    print(pandigitals)
    final = 0
    for next in pandigitals:
        if is_prime(next):
            final = next
            break
    return final


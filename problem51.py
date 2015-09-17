"""
Prime Digit Replacements
Project Euler Problem #51
by Muaz Siddiqui

By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, is the smallest prime 
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily 
adjacent digits) with the same digit, is part of an eight prime value family.
"""
from euler_helpers import timeit, primes_to, is_prime

def prime_family(prime, digit):
    members = 0
    for dig in "0123456789":
        next = int(prime.replace(digit, dig))
        if is_prime(next) and next > 100000:
            members += 1
    return members == 8

@timeit
def answer():
    # Looking for 6-digit number with exactly 3 repeating digits not including
    # the last one since then the family could not contain 8 primes, furthermore
    # the smallest prime must have repeating digits 0, 1, or 2 in order for the 
    # family to have eight members
    primes = primes_to(1000000, 100000)
    for prime in primes:
        next = str(prime)
        if next.count('0') == 3 and prime_family(next, '0') \
        or next.count('1') == 3 and prime_family(next, '1') and next[:-1] != 1\
        or next.count('2') == 3 and prime_family(next, '2'):
            return next

"""
Trunctable primes
Project Euler Problem #37
by Muaz Siddiqui

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage: 
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, 
and 3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.
"""
from euler_helpers import timeit, is_prime

def is_trunctable(n):
    if not is_prime(n):
        return False
    else:
        temp = n//10
        temp2 = n%10
        dividend = 10
        while temp != 0:
            if not is_prime(temp):
                return False
            temp = temp//10
        while dividend < n:
            if not is_prime(temp2):
                return False
            dividend *=10
            temp2 = n % dividend
        return True

@timeit
def answer():
    count = []
    x = 12 
    while len(count) < 11:
        if is_trunctable(x):
            count.append(x)
        x += 1
    return sum(count)
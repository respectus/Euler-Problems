"""
Prime permutations
Project Euler Problem #49
by Muaz Siddiqui

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 
3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each
 of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from euler_helpers import timeit, primes_to, is_prime, is_perm

# Must be increasing arithmetic sequence, prime, and permutation
# The most limiting of these within 1000 to 10000 is the prime stipulation
# Construct list of primes and check other properties

@timeit
def answer():
    # Lower bound is 1487
    found = 0
    primes = primes_to(10000, 1487)
    for a in range(len(primes)):
        for b in range(a+1, len(primes)):
            prime_a = primes[a]
            prime_b = primes[b]
            c = prime_b + (prime_b - prime_a)
            if c < 10000 and is_prime(c):
                if is_perm(prime_a, prime_b) and is_perm(prime_a, c):
                    found = str(prime_a) + str(prime_b) + str(c)
                    break
        if found:
            break
    return found




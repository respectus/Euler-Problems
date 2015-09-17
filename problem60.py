"""
Prime pair sets
Project Euler Problem #60
by Muaz Siddiqui

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and 
concatenating them in any order the result will always be prime. For example, 
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, 
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate 
to produce another prime.
"""
from euler_helpers import timeit, is_prime, primes_to
import itertools
prime_list = primes_to(8400)

def is_prime_set(primes):
    return all(is_prime(int(str(prime[0]) + str(prime[1]))) for prime in itertools.permutations(primes, 2))

def prime_pairs(primes, length):
    if len(primes) == length:
        return primes
    for prime in prime_list:
        check = primes + [prime]
        if prime > primes[-1] and is_prime_set(check):
            next = prime_pairs(check, length)
            if next:
                return next
    return 0

@timeit
def answer():
    while True:
        pairs = prime_pairs([prime_list.pop(0)], 5)
        if pairs:
            print(pairs)
            return sum(pairs)

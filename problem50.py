"""
Consecutive Prime Sum
Project Euler Problem #50
by Muaz Siddiqui

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below 
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive 
primes?
"""
from euler_helpers import timeit, primes_to, is_prime

@timeit
def answer(n):
    length = 0
    longest = 0
    primes = primes_to(n)
    # Make a list of sums
    prime_sum = [0]
    for x in range(len(primes)):
        prime_sum.append(prime_sum[x] + primes[x])
    for a in range(len(prime_sum)):
        b = a - (length + 1)
        while b >= 0:
            dif = prime_sum[a] - prime_sum[b]
            if dif > n:
                b -=1
                break
            if is_prime(dif):
                length = a - b
                longest = dif
            b -=1
    print("The prime is: " + str(longest) + " and consists of " + str(length) + " primes.")




"""
Quadratic Primes
Project Euler Problem #27
by Muaz Siddiqui

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values 
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible 
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes 
for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 
1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with 
n = 0.
"""

# Since we have n^2 + n + 41 producing 40 primes and n = 0 must be primes we 
# can reduce the amount of b's to check by b > -(40^2 + 40a) and b must be primes
def is_prime(num):
        if num <= 3:
            if num <= 1:
                return False
            return True
        if not num % 2 or not num % 3:
            return False
        for i in range(5, int(num**0.5) + 1, 6):   
            if not num%i or not num%(i + 2):
                return False
        return True


def answer():
    max_a, max_b, longest_seq = 0, 0, 0
    for a in range(-1000, 1001):
        for b in range(1, 1001):
            if is_prime(b):
                if b > (-40**2 -40*a) and b > longest_seq:
                    n, seq = 0, 0
                    while is_prime(n**2 + a*n +b):
                        seq += 1
                        n += 1
                    if seq > longest_seq:
                        max_a, max_b, longest_seq = a, b, seq
    print(longest_seq)
    return max_a * max_b













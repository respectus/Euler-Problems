import functools
# Find the prime factorization of the given number, returned as an array
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

# Number of factors is product of the (exponent + 1) of all prime factors
def num_factors(n):
    prime_factors = primes(n)
    exponents = []
    while len(prime_factors) > 0:
        next = prime_factors[0]
        count = prime_factors.count(next)
        exponents.append(count + 1)
        prime_factors = [item for item in prime_factors if item != next]

    return functools.reduce(lambda x, y: x*y, exponents)

#76576500
def answer():
    x = 1
    next_tri = 1
    while True:
        x += 1 
        next_tri += x
        if num_factors(next_tri) > 500:
            return next_tri 
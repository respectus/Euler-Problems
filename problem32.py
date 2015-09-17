"""
Pandigital Products
Project Euler Problem #32
by Muaz Siddiqui

We shall say that an n-digit number is pandigital if it makes use of all the digits 
1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 
pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.
"""

def is_pandigital(num):
    return len(str(num)) == 9 and not "123456789".strip(str(num))

def answer():
    pandigitals = set()
    for i in range(2,98):
        first = 123 if i > 10 else 1234
        for n in range(first, 10000//i):
            product = i*n
            if is_pandigital(str(i) + str(n) + str(product)):
                pandigitals.add(product)
    return sum(pandigitals)


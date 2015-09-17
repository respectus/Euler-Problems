"""
Amicable Chains
Project Euler Problem #95
by Muaz Siddiqui

The proper divisors of a number are all the divisors excluding the number itself. 
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these 
divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the 
proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 
220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, 
we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding 
one million.
"""
from euler_helpers import timeit

@timeit
def answer():
    max_ = 0
    min_ = 1000000
    divisors = [1] * min_
    for n in range(2, min_//2):
        for a in range(2*n, min_, n):
            divisors[a] += n

    for n in range(2, 1000000):
        x, chain = n, []
        while divisors[x] < 1000000:
            divisors[x], x =  1000001 , divisors[x] 
            if x in chain:
                ind = chain.index(x)
                length = len(chain[ind:])
                #print(length)
            else:
                chain.append(x)
                continue
            if length > max_:
                max_ = length
                min_ = min(chain[ind:])

    return min_



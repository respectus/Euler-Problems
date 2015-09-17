"""
Digit factorial chains
Project Euler Problem #74
by Muaz Siddiqui

The number 145 is well known for the property that the sum of the factorial of its 
digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers 
that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck 
in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest 
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty 
non-repeating terms?
"""
from euler_helpers import timeit, factorial, memoize

factorials = [factorial(n) for n in range(10)]
chain = []

@memoize
def factorial_chain(n):
    global chain
    chain.append(n)
    next = sum(factorials[int(dig)] for dig in str(n))
    if next in chain:
        return 1
    chain.append(next)
    return 1 + factorial_chain(next)
        

@timeit
def answer():
    global chain
    count = 0
    for n in range(1,1000000):
        if factorial_chain(n) == 60:
            count += 1
        chain = []
    return count
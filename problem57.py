"""
Square root convergents
Project Euler Problem #57
by Muaz Siddiqui

It is possible to show that the square root of two can be expressed as an infinite 
continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 
1393/985, is the first example where the number of digits in the numerator exceeds 
the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with 
more digits than denominator?
"""
from euler_helpers import timeit
from fractions import Fraction

def root_2(answer):
    while len(answer) != 1000:
        answer.append(1 + 1/(1 + answer[-1]))
    return answer

@timeit
def answer():
    roots = [(3, 2)]
    for x in range(1, 1000):
        roots.append([roots[x - 1][0] + roots[x - 1][1]*2, roots[x - 1][0] + roots[x - 1][1]])
    count = 0
    for root in roots:
        if len(str(root[0])) > len(str(root[1])):
            count += 1
    return count
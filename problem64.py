"""
Odd Period Square Roots
Project Euler Problem #64
by Muaz Siddiqui

All square roots are periodic when written as continued fractions and can be written
in the form:

It can be seen that the sequence is repeating. For conciseness, we use the notation 
√23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
"""
from euler_helpers import timeit, is_square

def square_continued(num):
    # Continued fraction expansion can be done iteratively
    m = 0
    d = 1
    a = int(num**0.5)
    seen = []
    period = []
    while True:
        m = d*a - m
        d = (num - m**2)/d
        a = int((int(num**0.5)+m)/d)
        next = (m, d, a)
        if a == 50:
            return period
        if next in seen:
            return period
        seen.append(next)
        period.append(a)

@timeit
def answer():
    count = 0
    for n in range(2, 10001):
        if is_square(n):
            continue
        if len(square_continued(n))%2:
            count += 1
    return count

"""
Arithmetic Expressions
Project Euler Problem #93
by Muaz Siddiqui

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use 
of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is 
possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target 
numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained 
before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of 
consecutive positive integers, 1 to n, can be obtained, giving your answer as a 
string: abcd.
"""
from euler_helpers import timeit
from operator import add, mul, sub, truediv
import itertools

@timeit
def answer():
    # Since this problem involves a lot of permutations I looked up methods in 
    # itertools
    longest = 0
    sets = []
    for nums in itertools.combinations(range(1,10), 4):
        next = []
        for num in itertools.permutations(nums):
            for operator in itertools.product([add, mul, sub, truediv], repeat=3):
                a = operator[0](operator[1](num[0],num[1]),operator[2](num[2],num[3]))
                if a > 0 and a == int(a):
                    next.append(a)
                b = operator[0](operator[1](operator[2](num[0],num[1]),num[2]), num[3])
                if b > 0 and b == int(b):
                    next.append(b)
            count = 1
            while count in next:
                count += 1
            if count - 1 > longest:
                longest = count - 1
                sets = num
    return ''.join(str(x) for x in sorted(sets))



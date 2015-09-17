"""
Pandigital Multiples
Project Euler Problem #38
by Muaz Siddiqui

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
from euler_helpers import timeit, is_pandigital

@timeit
def answer():
    #Largest single integer * (1-n) is with 9, 918273645
    max_ = 918273645
    # n > 1 so the minimum it can be is 2 aka the max we can go up to is 9876
    for x in range(10, 9877):
        next = str(x)
        start = 2
        while len(next) < 9:
            next = next + str(x*start)
            start += 1
        next = int(next)
        if is_pandigital(next):
            max_ = max(max_, next)
    return max_

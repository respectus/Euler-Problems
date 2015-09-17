"""
Square Digit Chains
Project Euler Problem #92
by Muaz Siddiqui

A number chain is created by continuously adding the square of the digits in a 
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89? 
"""
from euler_helpers import timeit

def check_chain(num):
    sum_ = 0
    for dig in str(num):
        dig = int(dig)
        sum_ += dig * dig
    return sum_

@timeit
def answer():
    # The max for the next number in the chain will be 9^2 * 7 spots so 567
    cache = [0] * 568
    count = 0
    for i in range(1, len(cache)):
        next = check_chain(i)
        while next > i and next != 89:
            next = check_chain(next)
        if cache[next] or next == 89:
            cache[i] = 1
            count += 1
    for i in range(len(cache), 10000001):
        if cache[check_chain(i)]:
            count += 1
    return count

        



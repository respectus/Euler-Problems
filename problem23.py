"""
Non-abundant sums
Project Euler Problem #23
by Muaz Siddiqui

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
that can be written as the sum of two abundant numbers is 24. By mathematical 
analysis, it can be shown that all integers greater than 28123 can be written as 
the sum of two abundant numbers. However, this upper limit cannot be reduced any 
further by analysis even though it is known that the greatest number that cannot 
be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def d(x):
    proper_divisors = []
    for num in range(x//2):
        if x%(num+1) == 0:
            if (num+1) not in proper_divisors:
                proper_divisors.append(num+1)
                proper_divisors.append(x//(num+1))
    if x in proper_divisors:
        proper_divisors.remove(x)
    return sum(set(proper_divisors))

# List all abundant nums under 28123
def abundant_nums():
    abundant = []
    for num in range(28123):
        if num < d(num):
            abundant.append(num)
    return abundant

def answer():
    not_sum_abundant = []
    abundants = abundant_nums()
    for num in range(28123):
        i = 0
        is_abundant = False
        while abundants[i] < num:
            if num - abundants[i] in abundants:
                is_abundant = True
                break
            i += 1
        if not is_abundant:
            not_sum_abundant.append(num)
    return sum(not_sum_abundant)

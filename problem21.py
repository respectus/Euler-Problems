"""
Amicable Numbers
Project Euler Problem #21
by Muaz Siddiqui

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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
    return sum(proper_divisors)

def answer():
    amicable_numbers = []
    for x in range(10001):
        if x not in amicable_numbers:
            this = d(x)
            next = d(this)
            # important a != b
            if x == next and x != this:
                amicable_numbers.append(x)
                amicable_numbers.append(this)
    return sum(amicable_numbers)
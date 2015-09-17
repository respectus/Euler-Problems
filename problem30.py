"""
Digit Fifth Powers
Project Euler Problem #30
by Muaz Siddiqui

Surprisingly there are only three numbers that can be written as the sum of fourth
powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of
their digits.
"""
# This can be brute forced, but there is an upper bound at 6 * 9^5 since
# a greater number of digits would surely go over as the digits are raised to the fifth power

def digit_powers(n):  
    # Precalculate each digits' power    
    digit_pows = [i ** n for i in range(10)]   
    pow_sum = 0
    upper = (n + 1) * digit_pows[9]
    for num in range(10, upper + 1):
        tempsum = tempnum = num
        # Chop last digit
        while tempnum:
            tempsum -= digit_pows[tempnum % 10]
            tempnum //= 10
        # Evenly divides here so add to pow_sum
        if tempsum == 0:
            pow_sum += num
    return pow_sum

def answer():
    return digit_powers(5)
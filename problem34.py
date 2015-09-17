"""
Digit factorials
Project Euler Problem #34
by Muaz Siddiqui

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

# Since 9! * 8 = 7-digits so up to 7 digits in answer. 9! * 7 = 2540160

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def answer():
    digit_factorial = [1] + [factorial(n) for n in range(1,10)]
    sums = 0
    for x in range(3, 2540161):
        if sum(digit_factorial[digit] for digit in map(int, (dig for dig in str(x)))) == x:
            sums += x
    return sums

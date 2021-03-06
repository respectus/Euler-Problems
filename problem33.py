"""
Digit cancelling fractions
Project Euler Problem #33
by Muaz Siddiqui

The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which 
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less 
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator."""
def gcd(numerator, denominator):
    while denominator:
        numerator, denominator = denominator, numerator % denominator
    return numerator

def answer():
    numerator = 1
    denominator = 1
    for x in range(10, 100):
        for y in range(10, 100):
            # number can't have a 0 at the end
            if x%10 != 0 and y%10 != 0 and y > x:
                if x%10 == y%10 and (x//10)/(y//10) == x/y:
                    numerator *= x
                    denominator *= y
                elif x%10 == y//10 and (x//10)/(y%10) == x/y:
                    numerator *= x
                    denominator *= y
                elif x//10 == y%10 and (x%10)/(y//10) == x/y:
                    numerator *= x
                    denominator *= y
                elif x//10 == y//10 and (x%10)/(y%10) == x/y:
                    numerator *= x
                    denominator *= y
                else:
                    continue
    return denominator / gcd(numerator, denominator)

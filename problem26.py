"""
Reciprocal Cycles
Project Euler Problem #26
by Muaz Siddiqui

A unit fraction contains 1 in the numerator. The decimal representation of the 
unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.
"""

# All rational numbers either have repeating or terminating decimals
# No brute force this time! Maths can help :)
# Only odd denominators will lead to repeating decimals
# Prime denominators will have the longest reptend(portion which repeats)
# Reptend has length equal to the order of 10 mod p 
# (aka order=k where 10^k = 1 mod p)
def length_of_reptend(num):
    for k in range(1, num):
        if (10 ** k) % num == 1:
            return k, num
    return 0, num

def answer():
    reptends = [length_of_reptend(num) for num in range(2, 1001)]
    best = 0
    longest = 0
    for length, num in reptends:
        if length > longest:
            best = num
            longest = length
    return best







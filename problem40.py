"""
Champernowne's constant
Project Euler Problem #40
by Muaz Siddiqui

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the 
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from euler_helpers import timeit

@timeit
def answer():
    string = ""
    count = 1
    while len(string) < 1000000:
        string += str(count)
        count += 1
    return int(string[0]) *  int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999]) 
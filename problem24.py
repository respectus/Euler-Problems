"""
Lexicographic Permutations
Project Euler Problem #24
by Muaz Siddiqui

A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def perms(digits):
    if not digits:
        return [[]]
    all_perms = []
    for digit in digits:
        not_digit = digits[:]
        not_digit.remove(digit)
        all_perms.extend([[digit] + next for next in perms(not_digit)])
    return all_perms

def answer():
    return perms([0,1,2,3,4,5,6,7,8,9])[999999]

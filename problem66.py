"""
Diophantine Equation
Project Euler Problem #66
by Muaz Siddiqui

Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained 
when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value 
of x is obtained.
"""
from euler_helpers import timeit, is_square, square_continued
import itertools
""" These Diophantine equations take the form of Pell's Equation, in order to 
minimize x we can take the coninued fraction and test the numerator as x
test the denominator as y and hope to find minimal solution """

# Takes in D and returns the minimal x
def solve_pells(num):
    if is_square(num):
        return 0

    # b_n is found by square_continued and a_n is always 1
    guess = int(num**0.5)
    b = square_continued(num)
    #A_1 and B_1 given by A_1/B_1 = ((b1*b0) + a1)/b1
    numerator = [guess, guess*b[0] + 1]
    denominator = [1, b[0]]
    if numerator[1]**2 - num*denominator[1]**2 == 1:
        return numerator[1]
    for n in itertools.count(2):
        # A_n = b_n * A_n-1 + a_n* A_n-2 where A_n is approx numerator
        # B_n = b_n * B_n-1 + a_n* A_n-2 where B_n is approx denominator
        x = b[(n-1)%len(b)] * numerator[n-1] + numerator[n-2]
        y = b[(n-1)%len(b)] * denominator[n-1] + denominator[n-2]
        if x**2 - num*y**2 == 1:
            return x 
        numerator.append(x)
        denominator.append(y)

@timeit
def answer():
    max_ = 0
    best_x = 0
    for n in range(2,1001):
        next = solve_pells(n)
        if next > max_:
            max_ = next
            best_x = n
    return best_x 


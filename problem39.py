"""
Integer Right Triangles
Project Euler Problem #39
by Muaz Siddiqui

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from euler_helpers import timeit

def right_solutions(n):
    count = 0
    for a in range(2, n//3):
        for b in range(n//2 - a, n//2):
            if (n-a-b) == ((a**2 + b**2) ** 0.5):
                count += 1
    return count

@timeit
def answer():
    max_ = 0
    for p in range(12, 1001):
        next = right_solutions(p)
        if next > max_:
            max_ = next
            best_p = p
    return best_p



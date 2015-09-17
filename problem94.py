"""
Almost Equilateral Triangles
Project Euler Problem #94
by Muaz Siddiqui

It is easily proved that no equilateral triangle exists with integral length sides 
and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 
square units.

We shall define an almost equilateral triangle to be a triangle for which two sides 
are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral 
side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""
from euler_helpers import timeit
@timeit
def answer():
    sum_ = 0
    perimeter = 0
    # Flip sign to add one or subtract one from the perimeter
    sign = 1
    a, b = 1, 1
    while perimeter < 1000000000:
        a, b = b, 4*b - a + 2*sign
        sum_ += perimeter
        perimeter = 3*b + sign
        sign = - sign
    return sum_
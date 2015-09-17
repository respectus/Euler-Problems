"""
Counting Rectangles
Project Euler Problem #85
by Muaz Siddiqui

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution.
"""
from euler_helpers import timeit

# The formula f(x,y) = ((x^2 +x)*(y^2+y))/4 gives the number of rectangles in a 
# rectangle of dimensions x,y.
@timeit
def answer():
    min_ = 2000000
    x = 2
    y = min_//6
    while x <= y:
        # Finds nearest to 2 million rectangles
        difference = abs(x*(x+1)* y*(y+1)/4 - 2000000)
        if difference < min_:
            area = x * y
            min_ = difference
        x += 2
        y = int((2000000*4/(x*(x+1)))**0.5)
    return area

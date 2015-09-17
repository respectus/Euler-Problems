"""
Right Triangles with integer coordinates
Project Euler Problem #91
by Muaz Siddiqui

Each of the six faces on a cube has a different digit (0 to 9) written on it;
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are 
joined to the origin, O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be formed 
when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed? 
"""
from euler_helpers import timeit, gcd
# Most triangles can be given by 3n^2 the rest can be found using
# min(max_x-x_1/dx, y_1/dy)
@timeit
def answer():
    # 3*50*50 = 7500
    count = 7500
    for x in range(1, 51):
        for y in range(1, 50):
            a = gcd(x, y)
            count += min(x*a//y, a*(50-y)//x) * 2
    return count
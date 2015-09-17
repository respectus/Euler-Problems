"""
Magic 5-gon Ring
Project Euler Problem #68
by Muaz Siddiqui

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each 
line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest 
external node (4,3,2 in this example), each solution can be described uniquely. For 
example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. 
There are eight solutions in total.

Total   Solution Set
9   4,2,3; 5,3,1; 6,1,2
9   4,3,2; 6,2,1; 5,1,3
10  2,3,5; 4,5,1; 6,1,3
10  2,5,3; 6,3,1; 4,1,5
11  1,4,6; 3,6,2; 5,2,4
11  1,6,4; 5,4,2; 3,2,6
12  1,5,6; 2,6,4; 3,4,5
12  1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum 
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 
16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon 
ring?
"""
from euler_helpers import timeit
""" This solution can be simplified with some thought, since it's a 16-digit
string and we are trying to maximize the string the 10 should be on the external
node and we should have the 6, 7, 8, and 9 on the external node. The total sum
should be 6+7+8+9+10+ 2*(1+2+3+4+5)=70 since the internal nodes are counted twice
therefore each line (magic sum) must be 70/5 = 14."""
@timeit
def answer():
    # line 1 must be 14 and 14-6 = 8 the only nums in 1-5 that add to 8 are 5,3
    lines = [[6,5,3], [10,0,0], [9,0,0], [8,0,0], [7,0,0]]
    for n in range(1,len(lines)):
        total = 0
        for x in range(len(lines[n])):
            if x == 0:
                total += lines[n][0]
            if x == 1:
                lines[n][x] = lines[n-1][2]
                total += lines[n-1][2]
            if x == 2:
                lines[n][x] = 14 - total
    for x in range(len(lines)):
        lines[x] = ''.join([str(dig) for dig in lines[x]])
    return (''.join(lines))




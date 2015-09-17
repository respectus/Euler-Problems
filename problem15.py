import math
# To get to the bottom m + n moves and m ways to go down, n ways to go right
# m+n C n or m+n C m
def lattice_paths(m, n):
    f = math.factorial
    return f(m + n)/(f(m)*f(n))

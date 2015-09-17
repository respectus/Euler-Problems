"""
Singular Integer Right Triangles
Project Euler Problem #75
by Muaz Siddiqui

It turns out that 12 cm is the smallest length of wire that can be bent to form an 
integer sided right angle triangle in exactly one way, but there are many more 
examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer 
sided right angle triangle, and other lengths allow more than one solution to be 
found; for example, using 120 cm it is possible to form exactly three different 
integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can 
exactly one integer sided right angle triangle be formed?
"""
from euler_helpers import timeit
import numpy as np
"""
We generate all the primitive Pythagorean triples and check their multiples up to
1,500,000 by creating a primitive tree with the root at (3,4,5) and by using
F.J.M Barnings matrices to generate 3 children. 
"""
a = np.matrix('1 -2 2; 2 -1 2; 2 -2 3')
b = np.matrix('1 2 2; 2 1 2; 2 2 3')
c = np.matrix('-1 2 2; -2 1 2; -2 2 3')

def generate_children(triple):
    root = np.array(triple)
    child1 = a.dot(root).tolist()
    child2 = b.dot(root).tolist()
    child3 = c.dot(root).tolist()
    return [child1[0], child2[0], child3[0]]

def make_primitive_tree(limit):
    tree = [[3,4,5]]
    leaves = generate_children([3,4,5])
    found = False
    next = []
    while True:
        for leaf in leaves:
            perimeter = sum(leaf)
            if perimeter <= limit:
                tree.append(leaf)
                next.extend(generate_children(leaf))
            else:
                found = True
        if found:
            return tree
        leaves = next

@timeit
def answer():
    limit = 1500000
    primitive_triples = make_primitive_tree(limit)
    wires = [0] * (limit + 1)
    count = 0
    # for each triple check all it's
    for triple in primitive_triples:
        length = sum(triple)
        wire = length
        while(wire <= limit):
            wires[wire] += 1
            if wires[wire] == 1:
                count += 1
            if wires[wire] == 2:
                count -= 1
            wire += length
    return count

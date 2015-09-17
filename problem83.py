"""
Path Sum: Four Ways
Project Euler Problem #83
by Muaz Siddiqui

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom 
right, by moving left, right, up, and down, is indicated in bold red and is equal 
to 2297.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right 
by only moving right and down.
"""
from euler_helpers import timeit
import networkx

@timeit
def answer():
    f = open('p081_matrix.txt', 'r')
    data = [list(map(int,row.split(','))) for row in f.read().split()]
    """
    This time we can use a graph and find the Dijkstra path from the top to
    bottomr right.
    """
    graph = networkx.DiGraph()
    # Represents Down, Left, Up, Right
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    for a in range(80):
        for b in range(80):
            neighbors = [(a+x,b+y) for x, y in directions if 0<= a+x < 80 and 0<= b+y < 80]
            for x, y in neighbors:
                graph.add_edge((a,b), (x,y), weight = data[x][y])
    shortest_path = data[0][0] + networkx.dijkstra_path_length(graph, source=(0,0), target=(79,79))
    return shortest_path
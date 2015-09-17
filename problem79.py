"""
Passcode Derivation
Project Euler Problem #79
by Muaz Siddiqui

A common security method used for online banking is to ask the user for three 
random characters from a passcode. For example, if the passcode was 531278, they 
may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so 
as to determine the shortest possible secret passcode of unknown length.
"""
from euler_helpers import timeit
from toposort import toposort

@timeit
def answer():
    f = open('p079_keylog.txt', 'r')
    data = list(set(map(int, f.read().split())))
    graph = {}
    for datum in data:
        datum = str(datum)
        if datum[2] in graph:
            graph[datum[2]] |= {datum[0], datum[1]}
        else:
            graph[datum[2]] = {datum[0], datum[1]}
        if datum[1] in graph:
            graph[datum[1]] |= {datum[0]}
        else:
            graph[datum[1]] = {datum[0]}
    graph = list(map(list, list(toposort(graph))))
    graph = [item[0] for item in graph]
    return ''.join(graph)

"""
Su Doku
Project Euler Problem #96
by Muaz Siddiqui

Su Doku (Japanese meaning number place) is the name given to a popular puzzle 
concept. Its origin is unclear, but credit must be attributed to Leonhard Euler 
who invented a similar, and much more difficult, puzzle idea called Latin Squares. 
The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in 
a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the 
digits 1 to 9. Below is an example of a typical starting puzzle grid and its 
solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, 
although it may be necessary to employ "guess and test" methods in order to 
eliminate options (there is much contested opinion over this). The complexity of 
the search determines the difficulty of the puzzle; the example above is considered 
easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains 
fifty different Su Doku puzzles ranging in difficulty, but all with unique 
solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top 
left corner of each solution grid; for example, 483 is the 3-digit number found 
in the top left corner of the solution grid above.
"""
from euler_helpers import timeit

sum_ = 0
last = []

def go_to_last_valid(puzzle):
    global last
    prev = last.pop()
    prev_index = prev[1]
    prev_value = prev[0]
    if prev_value + 1 <= 9:
        last.append([prev_value+1, prev_index])
        rest = set()
        for a in range(81):
            if prev_index/9 == a/9 or not (prev_index - a) % 9 or (prev_index/27 == a/27 and (prev_index%9)/3 == (a%9)/3):
                rest.add(puzzle[a])
        rest.remove('0')

        if len(rest) == 9:
            prev = go_to_last_valid(puzzle)
        
        for num in '123456789'[:prev_value]:
            if num not in rest:
                last.append([int(num), blank])
                fill_puzzle(puzzle[:blank] + num + puzzle[blank + 1:])
                break
        puzzle = puzzle[:prev_index] + '0' + puzzle[prev_index + 1:]
        go_to_last_valid(puzzle)
    else:
        puzzle = puzzle[:prev_index] + '0' + puzzle[prev_index + 1:]
        go_to_last_valid(puzzle)

def fill_puzzle(puzzle):
    global sum_
    global last
    blank = puzzle.find('0')
    
    #puzzle finished!
    if blank == -1:
        sum_ += int(puzzle[:3])
        print(puzzle[:3],sum_)
        last = []
        return

    rest = set()
    for a in range(81):
        if blank/9 == a/9 or not (blank - a) % 9 or (blank/27 == a/27 and (blank%9)/3 == (a%9)/3):
            rest.add(puzzle[a])

    rest.remove('0')

    if len(rest) == 9:
        prev = go_to_last_valid(puzzle)
        
    for num in '123456789':
        if num not in rest:
            last.append([int(num), blank])
            fill_puzzle(puzzle[:blank] + num + puzzle[blank + 1:])
            break

@timeit
def answer():
    f = open('p096_sudoku.txt', 'r').readlines()
    data = ''.join(line[:9] for line in f if not 'Grid' in line)
    data = [data[n:(n+81)] for n in range(0, len(data), 81)]

    for puzzle in data:
        fill_puzzle(puzzle)

    return sum_

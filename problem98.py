"""
Anagramic squares
Project Euler Problem #98
by Muaz Siddiqui

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362.
What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962.
We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may
a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""
from euler_helpers import timeit

last = []

@timeit
def answer():
    f = open('p098_words.txt', 'r').read()
    data = f.split("\",")
    count = 0
    numAnagrams = 0
    longest = 0
    anagrams = []
    data2 = []
    for word in data:
        count += 1
        word = word.replace("\"", "")
        # Start with word here
        wlist = list(word)
        wlist.sort()
        word2 = ''.join(wlist)
        data2.append((word2, word, count))
    data2.sort()
    for i in range(len(data2) - 1):
        if(data2[i][0] == data2[i+1][0]):
            numAnagrams += 1
            print((numAnagrams, data2[i][1], data2[i+1][1]))
            if(len(data2[i][1]) > longest):
                longest = len(data2[i][1])
            anagrams.append((data2[i][1], data2[i+1][1]))
    squares = []
    square = 0
    numSquares = 1 
    while len(str(square)) < longest:
        square = numSquares ** 2
        numSquares += 1
        squares.append(square)
    for i in range(len(squares)):
        squares[i]



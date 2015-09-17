"""
Names Scores
Project Euler Problem #22
by Muaz Siddiqui

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical 
order. Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would 
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
# Converts name to alphabetical value
def name_to_num(name):
    alpha_value = 0
    for letter in name:
        alpha_value += ord(letter) - 64
    return alpha_value


def answer():
    f = open('names.txt', 'r')
    # Read all names and store as a list of names
    names = list(map(lambda x: x.replace("\"", "") ,f.read().split(",")))
    # Sort in alphabetical order
    names.sort()
    names = list(map(name_to_num, names))
    # Calculate values
    for x in range(len(names)):
        names[x] *= (x + 1)
    return sum(names)
    
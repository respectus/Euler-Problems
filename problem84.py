"""
Monopoly Odds
Project Euler Problem #84
by Muaz Siddiqui

A player starts on the GO square and adds the scores on two 6-sided dice to 
determine the number of squares they advance in a clockwise direction. Without 
any further rules we would expect to visit each square with equal probability: 
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) 
changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to 
go directly to jail, if a player rolls three consecutive doubles, they do not 
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands 
on CC or CH they take a card from the top of the respective pile and, after 
following the instructions, it is returned to the bottom of the pile. There are 
sixteen cards in each pile, but for the purpose of this problem we are only 
concerned with cards that order a movement; any instruction not concerned with 
movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. For this reason 
it should be clear that, with the exception of G2J for which the probability of 
finishing on it is zero, the CH squares will have the lowest probabilities, as 
5/8 request a movement to another square, and it is the final square that the 
player finishes at on each roll that we are interested in. We shall make no 
distinction between "Just Visiting" and being sent to JAIL, and we shall also 
ignore the rule about requiring a double to "get out of jail", assuming that 
they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can 
concatenate these two-digit numbers to produce strings that correspond with 
sets of squares.

Statistically it can be shown that the three most popular squares, in order, 
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. 
So these three most popular squares can be listed with the six-digit modal string: 
102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the 
six-digit modal string.
"""
from euler_helpers import timeit
import random

position = 0
chance_pos = 0
chest_pos = 0

def monopoly(dice, simulations):
    board = [0]*40
    doubles = 0
    global position

    def chance():
        chances = [0,10,11,24,39,5]
        global position
        global chance_pos
        chance_pos = (chance_pos + 1) % 16
        # Move to different spots
        if chance_pos < 6:
            position = chances[chance_pos]
        # Go to nearest railroad
        elif chance_pos == 6 or chance_pos == 7:
            if position == 7: position = 15
            if position == 22: position = 25
            if position == 36: position = 5
        # Go to nearest Utility
        elif chance_pos == 8:
            position = 28 if position == 22 else 12
        elif chance_pos == 9: position -= 3
        return

    def community_chest():
        chest = [0, 10]
        global chest_pos
        global position
        chest_pos = (chest_pos + 1) % 16
        if chest_pos < 2:
            position = chest[chest_pos]
        return

    for roll in range(simulations):
        dice1 = random.randint(1, dice) 
        dice2 = random.randint(1, dice)
        doubles = doubles + 1 if dice1 == dice2 else 0
        if doubles > 2:
            position = 10
            doubles = 0
        else:
            position = (position + dice1 + dice2) % 40

            # Chance
            if position == 7 or position == 22 == position == 36:
                chance()
            # Community Chest
            if position == 2 or position == 17 or position == 33:
                community_chest()
            # Go to Jail!
            if position == 30:
                position = 10 
        board[position] += 1

    string = ""
    print(board)
    for x in range(3):
        max_ = board.index(max(board))
        if max_ < 10:
            max_ = '0' + max_
        
        string += str(max_)
        board[max_] = 0
    return string
@timeit
def answer():
    return monopoly(4, 5000000)





























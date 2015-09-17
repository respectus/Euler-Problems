"""
Poker Hands
Project Euler Problem #54
by Muaz Siddiqui

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest 
value wins; for example, a pair of eights beats a pair of fives (see example 1 
below). But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); if the highest 
cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the first 
five are Player 1's cards and the last five are Player 2's cards. You can assume 
that all hands are valid (no invalid characters or repeated cards), each player's 
hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from euler_helpers import timeit

def does_one_win(player1, player2):
    first = calc_hand(player1)
    second = calc_hand(player2)
    if first[0] > second[0]:
        return True
    elif first[0] == second[0]:
        if first[1] > second[1]:
            return True
        elif first[1] == second[1]:
            if type(first[2]) != list:
                return first[2] > second[2]
            else:
                for x in range(len(first[2])):
                        if first[2][x] > second[2][x]: 
                            return True
                        elif first[2][x] == second[2][x]:
                            continue
                        else:
                            return False
        else:
            return False
    else:
        return False

# Values stores [rank of the hand, highest card in rank, list of next highest]
def calc_hand(hand):
    values = []
    joined = ''.join(hand)
    value = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
    straights = [(n, n-1, n-2, n-3, n-4) for n in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
    if 'A' in joined and 'K' in joined and 'Q' in joined and 'J' in joined and 'T' in joined\
        and (not joined.strip('AKQJTH') or not joined.strip('AKQJTC') or not joined.strip('AKQJTS') or not joined.strip('AKQJTD') ):
        values.append(10)
        return values
    score = [value[val[0]] for val in hand]
    score.sort()
    this_set = [card[0] for card in hand]
    # flush
    if len(set(card[1] for card in hand)) == 1:
        if score in straights:
            values.append(9)
            values.append(score[-1:])
            return values
        else:
            values.append(6)
            values.append(score[-1:])
            return values
    # four of a kind and full house
    elif len(set(this_set)) == 2:
        if this_set.count(this_set[0]) == 4:
            values.append(8)
            values.append(score[0])
            values.append(score[-1:])
            return values
        elif this_set.count(this_set[-1:]) == 4:
            values.append(8)
            values.append(score[-1:])
            values.append(score[0])
            return values
        else:
            if this_set.count(this_set[0]) == 3:
                values.append(7)
                values.append(score[0])
                values.append(score[-1:])
                return values
            else:
                values.append(7)
                values.append(score[-1:])
                values.append(score[0])
                return values

    elif score in straights:
        values.append(5)
        values.append(score[-1:])
        return values
    # 3 of a kind or two two of a kinds
    elif len(set(this_set)) == 3:
        if this_set.count(this_set[0]) == 3:
            values.append(4)
            values.append(this_set[0])
            values.append([score[-1:], score[-2:][0]])
            return values
        elif this_set.count(this_set[1]) == 3:
            values.append(4)
            values.append(this_set[1])
            values.append([score[-1:], score[-2:][0]])
            return values
        elif this_set.count(this_set[2]) == 3:
            values.append(4)
            values.append(this_set[2])
            values.append(score[::-1])
            return values
        else: 
            values.append(3)
            values.append(score[2])
            values.append(score[::-1])
            return values
    # two of a kind
    elif len(set(this_set)) == 4:
        values.append(2)
        values.append(score[2])
        values.append(score[::-1])
        return values
    else:
        values.append(1)
        values.append(score[-1:])
        values.append(score[:4])
        return values


@timeit
def answer():
    count = 5
    f = open('p054_poker.txt', 'r')
    hands = [line.strip().split(" ") for line in f.readlines()]
    for hand in hands:
        if does_one_win(hand[:5], hand[5:]):
            count += 1
    return count

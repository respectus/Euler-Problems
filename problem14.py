import sys
sys.setrecursionlimit(10000)

def hailstone(n):
    seq = []
    while n > 1:
        seq.append(n)
        if n%2 == 0:
            n = n//2
        else :
            n = 3*n + 1

    return len(seq) + 1 

def answer():
    hailstone_num = 1
    longest_chain = 0
    for num in range(1000000):
        curr_chain = hailstone(num)
        if curr_chain > longest_chain:
            longest_chain = curr_chain
            hailstone_num = num
    return hailstone_num

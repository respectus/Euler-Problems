import math

def powers_2():
    answer = math.fsum(map(int, str(2 ** 1000)))
    return answer
    
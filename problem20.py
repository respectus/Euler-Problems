import math


def factorial_digit_sum():
    answer = math.fsum(map(int, str(math.factorial(100))))
    return answer
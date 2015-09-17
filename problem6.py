from math import pow
def problem6():
    sum_of_sq = sum(x*x for x in range(101))
    sq_of_sum = pow(sum(x for x in range(101)), 2)
    return sq_of_sum - sum_of_sq



sum(x for x in range(101))**2 - sum(x*x for x in range(101))
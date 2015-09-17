import math

def problem5():
    high = math.factorial(20)
    numbers = [i+1 for i in range(20)]
    x = 40
    while x < high:
        if all(x % n == 0 for n in numbers):
            return x
    return high 


def factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n/2
    p = 3
    while n != 1:
        while n % p == 0:
            factors.append(p)
            n = n/p
        p += 2
    return factors
 

def factor_append(factors, new):
    if len(factors) == 0: return new
    for i in range(len(new)):
        if i > 0 and new[i] == new[i-1]: continue
        new_count = new.count(new[i])
        old_count = factors.count(new[i])
        if new_count > old_count:
            for j in range(new_count - old_count): factors.append(new[i])
    factors.sort()
    return factors
 

def smallest_evenly_divisible(num):
    F = []
    for i in range(1,num + 1):
        F = factor_append(F,factors(i))
    product = 1
    for i in F: product *= i
    return product
 

 
start = time.time()
product = smallest_evenly_divisible(20)
elapsed = (time.time() - start)

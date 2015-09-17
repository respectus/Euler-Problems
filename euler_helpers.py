import time, math, itertools

def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2) 

@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

@memoize
def is_palindrome(x):
    digits = []
    num = x
    while num > 0:
        if num < 10:
            digits.append(num)
        else: 
            digits.append(num % 10)
        num = num // 10
    def check_pal(n):
        if len(n) == 1:
            return False
        if len(n) == 2:
            return n[0] == n[1]
        elif len(n) == 3:
            return n[0] == n[2]
        elif n[0] == n[len(n) - 1]:
            return check_pal(n[1:len(n) -1])
        else:
            return False
    return check_pal(digits)
    
@memoize
def digital_sum(n):
    return sum([int(digit) for digit in str(n)])

@memoize
def is_palindrome2(x):
    return len(str(x)) != 1 and str(x) == (str(x)[::-1])

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r in %2.5f seconds' % (method.__name__, te-ts))
        return result

    return timed

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def primes_to(n, start = 3):
    primes = [2, 3] if start == 3 else []
    if not start%2:
        start += 1
    while start < n:
        start += 2 
        if is_prime(start):
            primes.append(start)
    return primes


def is_pandigital(num):
    return len(str(num)) == 9 and not "123456789".strip(str(num))

def perms(n):
    digit = [dig for dig in str(n)]
    final = list(set(itertools.permutations(digit)))
    return list(map(int, [''.join(num) for num in final]))

def is_perm(a, b):
    return sorted([dig for dig in str(a)]) == sorted([dig for dig in str(b)])

def word_to_num(word):
    alpha_value = 0
    for letter in word:
        alpha_value += ord(letter) - 64
    return alpha_value

def nums_to_letters(nums):
    message = []
    for num in nums:
        message.append(chr(num))
    return message

def letters_to_words(letters):
    words = []
    next = ""
    for letter in letters:
        if letter != " ":
            next += letter
        else:
            words.append(next)
            next = ""
    return " ".join(words)

def is_triangular(n):
    return (-1 + (1 + (8 * n))**0.5) % 2 == 0

def is_cube(num):
    return num == int(round(num**(1/3)))**3

def is_square(n):
    return not math.sqrt(n) % 1

def is_pentagonal(num):
    pent = (((24*num) + 1)** 0.5 + 1)/6
    return pent == math.floor(pent)

def is_hexagonal(num):
    hex_ = (((8*num) + 1)** 0.5 + 1)/4
    return hex_ == math.floor(hex_)

def is_heptagonal(n):
    return (3 + (9 + (40 * n))**0.5) % 10 == 0

def is_octagonal(n):
    return (2 + (4 + (12 * n))**0.5) % 6 == 0

def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while not n % d:
            primfac.append(d)
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

@memoize
def sum_proper_divsors(x):
    proper_divisors = []
    for num in range(x//2):
        if x%(num+1) == 0:
            if (num+1) not in proper_divisors:
                proper_divisors.append(num+1)
                proper_divisors.append(x//(num+1))
    if x in proper_divisors:
        proper_divisors.remove(x)
    return sum(proper_divisors)

def square_continued(num):
    # Continued fraction expansion can be done iteratively
    m = 0
    d = 1
    a = int(num**0.5)
    seen = []
    period = []
    while True:
        m = d*a - m
        d = (num - m**2)/d
        a = int((int(num**0.5)+m)/d)
        next = (m, d, a)
        if next in seen:
            return period
        seen.append(next)
        period.append(a)

def max_path_triangle(data):
    triangle = [list(map(int, row.split())) for row in data.splitlines()] 
    row = len(triangle) - 1
    while row > 0:
        for num in range(len(triangle[row]) - 1):
            # starting from the bottom sum the max of the two numbers below and the current number
            # going up the rows you will end with the max at the top
            triangle[row - 1][num] += max( triangle[row][num], triangle[row][num+1])
        row -= 1 
    return triangle[0][0]

def gcd(x, y):
    while x * y != 0:
        if x >= y:
            x = x % y
        else:
            y = y % x
    return x + y

def totient(n):
    primes = list(set(prime_factors(n)))
    phi = n
    for p in primes:
        phi *= (1 -(1/p))
    return phi

def extract_digs(num):
    digs = []
    for dig in str(num):
        digs.append(int(dig))
    return digs

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return list(filter(None, s))


@memoize
def count_change(value, coins=(1, 2, 5, 10, 20, 50, 100, 200)):
    if value == 0:
        return 1
    elif value < 0 or len(coins) == 0:
        return 0
    return count_change(value, coins[1:]) + count_change(value - coins[0], coins)

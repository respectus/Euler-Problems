def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)

# Clean memoized fibonacci calculator

def problem2():
    acc = 0 
    n = 1
    while fib(n) < 4000000:
        fibs = fib(n)
        if fibs % 2 == 0:
            acc += fibs
        n += 1
    return acc

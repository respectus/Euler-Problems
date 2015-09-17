def prime_10001():
    def is_prime(num):
        if num <= 3:
            if num <= 1:
                return False
            return True
        if not num % 2 or not num % 3:
            return False
        for i in range(5, int(num**0.5) + 1, 6):   
            if not num%i or not num%(i + 2):
                return False
        return True
    next = 2
    count = 1
    while count < 10001:
        next += 1
        if is_prime(next):
            count += 1
    print(next)

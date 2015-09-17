"""
Circular Primes
Project Euler Problem #35
by Muaz Siddiqui

The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
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

def perms(digits):
    rotate = []
    string = str(digits)
    for i in range(len(string) - 1):
        string = string[1:] + string[:1]
        rotate.append(string)
    return list(map(int, rotate))

def answer():
    circular = [2,3,5,7,11]
    primes = [2,5]
    count = 0
    # Generate all primes under 1 million that do not contain 2,4,5,6,8 since if those digits
    # were found at the end the number could not be prime
    for i in range(2, 1000000):
        string = str(i)
        # Take advantage of short-circuit eval and put is_prime at the end
        if '2' not in string and '4' not in string and '5' not in string and '6' not in string and '8' not in string and is_prime(i):
            primes.append(i)
    # For each prime check if all rotations are within the prime set
    for prime in primes:
        rotations =  perms(prime)
        all_prime = True
        for next in rotations:
            if next not in primes:
                all_prime = False
                break
        if all_prime:
            circular.extend(rotations)
    return len(set(circular))
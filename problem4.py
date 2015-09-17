
def is_Palindrome(x):
    digits = []
    num = x
    while num > 0:
        if num < 10:
            digits.append(num)
        else: 
            digits.append(num % 10)
        num = num // 10
    def check_pal(n):
        if len(n) == 2:
            return n[0] == n[1]
        elif len(n) == 3:
            return n[0] == n[2]
        elif n[0] == n[len(n) - 1]:
            return check_pal(n[1:len(n) -1])
        else:
            return False
    return check_pal(digits)

def find_max_palindrome(min=100,max=999):
    max_palindrome = 0
    for a in range(min,max + 1):
        for b in range(a + 1, max + 1): # avoid duplicates
            prod = a*b
            if prod > max_palindrome and str(prod)==(str(prod)[::-1]):
                max_palindrome = prod
    return max_palindrome

#906609

def problem4():
    x = 1000
    while x > 100:
        if is_Palindrome((x-1)*(x-2)):
            return (x-1)*(x-2)
        x -= 1
def problem9(n):
    for i in range(1,n):
        for j in range(1,n-i):
            k = n-i-j
            if i**2+j**2==k**2:
                return i*j*k
    return 0

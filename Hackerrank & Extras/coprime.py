m = int(input())
n = int(input())

def gcd(m, n):
    while n != 0:
        m,n = n, m % n
    return m 

def is_coprime(m,n):
    if gcd(m, n) == 1:
        print("Coprime")
    else:
        print("Not Coprime")

from math import sqrt
import random

LOWER = 10000
UPPER = 20000
alphabet = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']

def isPrime(nr):
    if nr < 1:
        return False
    elif nr == 2 or nr == 1:
        return True
    else:
        d = 3
        while d <= sqrt(nr):
                if nr % d == 0 or nr % 2 == 0:
                    return False
                d = d + 2
        return True

def generatePrimeNumber(lower, upper):
    nr = random.randint(lower, upper)
    if isPrime(nr):
        return nr
    else:
        return generatePrimeNumber(lower, upper)

def generatePQ():
    p = generatePrimeNumber(LOWER, UPPER)
    q = generatePrimeNumber(LOWER, UPPER)
    while p == q:
        q = generatePrimeNumber(LOWER, UPPER)
    return p, q

def computePhi(p, q):
    return (p-1)*(q-1)

def gcd(a, b):
    if a == b:
        return a
    else:
        if a > b :
            return gcd(a-b, b)
        else:
            return gcd(a, b-a)

def coprime(a, b):
    return gcd(a, b) == 1



if __name__ == '__main__':
    n = gcd(18, 36)
    print(n)
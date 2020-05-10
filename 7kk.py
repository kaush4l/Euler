# 10001st prime
import math


def isPrime(n):
    if n < 4:
        return True
    bool = True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            bool = False
    return bool

def nthPrime(n):
    num = 3
    while n - 2 > 0:
        num += 2
        if isPrime(num):
            n -= 1

    return num

print(nthPrime(10001))

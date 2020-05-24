# Summation of primes below a certain value

import math


def isPrime(n):
    if n < 4:
        return True
    bool = True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            bool = False
    return bool

def sumOfPrime(n):
    sum = 2
    for i in range(3, n , 2):
        if isPrime(i):
            sum += i
    return sum

print(sumOfPrime(2000000))

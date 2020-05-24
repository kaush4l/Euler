# Largest prime factor of a given number
import math

def remove2multiples(n):
    while n % 2 == 0:
        n = n / 2
    return n

def primeNumber(n):
    if n < 4:
        return True
    bool = True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            bool = False        
    return bool

def factorsCheck(n, max):
    for i in range(1, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            if primeNumber(n / i):
                if max < n/i:
                    max = n/i
            if primeNumber(i):
                if max < (n / i):
                    max = i
    return max

def largestPrimeFactor(n):
    m = remove2multiples(n)
    max = 1
    if n != m:
        max = 2
    return factorsCheck(m, max)

print(largestPrimeFactor(600851475143))

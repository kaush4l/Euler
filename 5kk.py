# GCD of first 20 numbers

# This answer was solved on paper
# Should write method to find the GCD of given numbers
def isPrime(n):
    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19]
    if n in primes:
        return True
    else:
        return False

def gcd(a, b):
    isCalculating = True
    while isCalculating:

# 232792560

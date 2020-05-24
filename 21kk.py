# Amicable numbers
# sum of factors of a number = number whose sum of factors is number
# d(a) = b and d(b) = a. a and b are amicable
import math

map = {}

def factors(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n / i)
    map[n] = int(sum(factors))
    return map[n]
        
def sum(n):
    sum = 0
    for i in n:
        sum += i
    return sum + 1

def amicableNumbers(max):
    sum = 0
    for num in range(1, max):
        added = factors(num)
        if added in map:
            sum += added + num
    return sum

print(amicableNumbers(10001)) # 31626 Supposed answer. Fix it

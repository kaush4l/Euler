# Factorial number digits sum

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

def add(n):
    p = str(n)
    sum = 0
    for digit in p:
        sum += int(digit)
    return sum

def factSum(n):
    return add(fact(n))

print(factSum(100))

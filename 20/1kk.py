def factorMultiple(n , num):
    maxQuotient = n /num
    return num * ((maxQuotient * (maxQuotient + 1)) / 2)

def multipleSum(n, a, b):
    print(factorMultiple(n, a) + factorMultiple(n, b) - factorMultiple(n, a*b))

print(multipleSum(999,3,5))

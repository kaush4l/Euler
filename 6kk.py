# Sum square difference
# For given n, (1 + .... + n)^2 - (1^2 + 2^2 + ......+ n^2)

def sum(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum

def squaresSum(n):
    array = []
    for i in range(1, n+1):
        array.append(i * i)
    return sum(array)

def numbersSum(n):
    p = (n * (n + 1)) / 2
    return int(p * p)

def squareDiff(n):
    return numbersSum(n) - squaresSum(n)

print(squareDiff(100))


def fib(n):
    a = 1
    b = 2
    sum = 2
    count = 0
    while b < n:
        b = b + a
        a = b - a
        count += 1
        if count == 3:
            count = 0
            sum += b
    return sum

print(fib(4000000))

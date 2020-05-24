def fib(n):
    a = 0
    b = 1
    index = 1 # starting with 1 as we are checking for b which is 1 extra
    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) == n:
            return index

print(fib(1000))

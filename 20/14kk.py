# Longest collatz path
# Collatz path
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

my_dict = {}

def longestChain(n):
    if n in my_dict :
        return my_dict[n]
    elif n != 1:
        if n % 2 == 0 :
            n = int(n / 2)
        else:
            n = (3 * n) + 1
        my_dict[n] = longestChain(n) + 1
        return my_dict[n]
    else:
        return 1

def longestChainNumber(n):
    max = 0
    num = 0
    for i in range(int(n/10), n):
        temp = longestChain(i)
        if max < temp:
            max = temp
            num = i
    return num

print(longestChainNumber(1000000))

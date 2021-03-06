# Triangular numbers generated by adding sequential numbers
# Number with the highest factors

import math


def div(n):
    sum = 1
    count = 0
    adder = 2
    while count < n:
        sum += adder
        adder += 1
        count = 0
        for num in range(1, int(math.sqrt(sum)+1)):
            if sum % num == 0:
                if num != sum/num:
                    count += 2
                else:
                    count += 1
        if count > n:
            return sum

print(div(500))

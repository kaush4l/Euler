# sum of digits in 2's nth power

def power2(pow):
    return 1 << pow

def powerAdd(pow):
    sum = 0
    for i in str(power2(pow)):
        sum += int(i)
    return sum

print(powerAdd(1000))

# No of ways to travel a matrix (lattice path)

def sumWays(n):
    n += 1
    matrix = n*[n*[0]]
    return matrixSum(matrix, 0, 0)[0][0]

def matrixSum(matrix, x, y):
    if x == len(matrix) - 1 and y == len(matrix) - 1:
        matrix[x][y] = 1
        return matrix
    # Optimization to half the calculation
    # ??
    xSum = 0
    if x != len(matrix) - 1:
        xSum = matrixSum(matrix,x + 1, y)[x + 1][y]
    ySum = 0
    if y != len(matrix) - 1:
        ySum = matrixSum(matrix, x, y + 1)[x][y + 1]
    # update value
    matrix[x][y] = int(xSum + ySum)
    return(matrix)

def method2(n):
    # 2n!/(n-r)!r! r = n
    # Using binomial coefficient
    nume = 1
    deno = 1
    for i in range(1, n + 1):
        deno *= i
    for i in range(n + 1, (2 * n) + 1):
        nume *= i
    return int(nume / deno)

# print(sumWays(2)) # 6
# print(sumWays(3)) # 20
# print(sumWays(4)) # 70
# print(method2(4)) 
# print(sumWays(5)) # 252
# print(method2(5)) 
# print(sumWays(6)) # 924
# print(method2(6)) 
# print(sumWays(7)) # 3432
# print(method2(7)) 
# print(sumWays(8)) # 12870
# print(method2(8)) 
# print(sumWays(9)) # 48620
# print(method2(9)) 
# print(sumWays(10)) # 184756
# print(method2(10)) 

# Loops increasing exponentially. Find relation
# Binomially related
print(method2(20))

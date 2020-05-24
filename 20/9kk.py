# Special Pythagorean triplet
# a^2 + b^2 = c^2
# For triplet where a + b + c = 1000 find abc
import math


def pythag(sum):
    for a in range(int(sum/3) - 1, 1 , -1):
        for b in range(int((sum - a) / 2), a, -1):
            c = sum - b - a
            if c > b and a*a + b*b == c*c:
                return a * b * c

print(pythag(1000))

# Largest palindrome product of a 3 digit number
def isPalindrome(num):
    s = str(num)
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s) -i - 1]:
            return False
    return True

def isPalindromeAlt(num): 
    s = str(num)
    # or even split string in half and reverse only half sting for further optimization
    if s == s[::-1]:
        return True
    return False

def maxNumber(n):
    max = 0
    for x in range(10**n, 10**(n-1), -1):
    # for x in range(10**(n-1), 10**n):
        for y in range(10**n, x, -1): # Checking till reduced loops by half and works 
        # for y in range(10**(n-1), 10**n):
            z = x * y
            if isPalindrome(z) and z > max:
                max = z
    return max

print(maxNumber(3))

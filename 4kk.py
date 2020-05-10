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

def maxNumber(): # Optimaztion to maybe take the number of digits as input and work on that
    max = 0
    for x in range(100, 1000): # Maybe not ideal as this is brute force
        for y in range(100, 1000): # But since Euler was just asking for answer
            z = x * y
            if isPalindrome(z) and z > max:
                max = z
    return max

print(maxNumber())

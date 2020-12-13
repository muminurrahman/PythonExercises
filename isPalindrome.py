def isPalindrome(inputString):
    inputString = inputString.upper()
    return inputString == inputString[::-1]


print(checkPalindrome("dad"))
print(checkPalindrome("Tenet"))
print(checkPalindrome("racecar"))
print()
print(checkPalindrome("egg"))
print(checkPalindrome("potato"))
print(checkPalindrome("car"))

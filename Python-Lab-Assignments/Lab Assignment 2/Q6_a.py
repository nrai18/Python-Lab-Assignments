# Question 6a: Check if number is palindrome.

# input - take number from user
num = int(input("Enter a number: "))

# computation - reverse number
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

# condition - check palindrome
if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
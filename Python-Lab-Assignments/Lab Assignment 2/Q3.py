# Question 3: Create a program to display reverse of number and sum of its digits.

# input - take number from user
num = int(input("Enter a number: "))

# computation - reverse number and calculate digit sum
rev = 0
sum_digits = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    sum_digits += digit
    temp //= 10

# output - display reversed number and digit sum
print("Reversed number:", rev)
print("Sum of digits:", sum_digits)
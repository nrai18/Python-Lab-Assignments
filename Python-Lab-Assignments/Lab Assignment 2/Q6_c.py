# Question 6c: Check if number is Armstrong.

# input - take number from user
num = int(input("Enter a number: "))

# computation - calculate armstrong sum
sum_pow = 0
temp = num
order = len(str(num))
while temp > 0:
    digit = temp % 10
    sum_pow += digit ** order
    temp //= 10

# condition - check armstrong
if num == sum_pow:
    print("Armstrong Number")
else:
    print("Not Armstrong")
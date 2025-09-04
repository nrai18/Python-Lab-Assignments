# Question 8b: Generate a Lower Right Triangle pattern.

# input - take number of rows from user
n = int(input("Enter number of rows: "))

# output - print the pattern
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
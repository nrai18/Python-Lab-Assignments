# Question 8a: Generate an Upper Right Triangle pattern.

# input - take number of rows from user
n = int(input("Enter number of rows: "))

# output - print the pattern
for i in range(n):
    print(' ' * i + '*' * (n - i))
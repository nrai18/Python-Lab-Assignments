# Question 8d: Generate Pascal's Triangle.

# input - take number of rows from user
n = int(input("Enter number of rows: "))

# output - print the pattern
for i in range(n):
    print(' ' * (n - i), end='')
    
    # The first number in any row is always 1
    num = 1
    for j in range(i + 1):
        print(num, end=' ')
        num = num * (i - j) // (j + 1)
    
    # Move to the next line after printing the row
    print()
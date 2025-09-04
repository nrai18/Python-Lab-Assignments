# Question 8c: Generate a pyramid for any character entered through keyboard.

# input - take number of rows and the character from user
n = int(input("Enter number of rows: "))
char = input("Enter the character to use: ")

# output - print the pattern
for i in range(n):
    print(' ' * (n - 1 - i) + char * (2 * i + 1))
# Question 4: Create a program to display tables for first n natural numbers.

# input - take n from user
n = int(input("Enter the value of n: "))

# computation - generate tables from 1 to n
for i in range(1, n+1):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()
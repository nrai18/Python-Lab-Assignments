# Question 2: Create a program to calculate factorial of a number entered from the console.

# input - take number from user
n = int(input("Enter a number: "))

# computation - calculate factorial using loop
fact = 1
for i in range(1, n+1):
    print(fact,i)
    fact *= i

# output - display factorial
print("Factorial of", n, "is", fact)
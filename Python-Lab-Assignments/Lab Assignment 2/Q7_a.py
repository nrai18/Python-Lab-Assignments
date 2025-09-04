# Question 7a: Generate Fibonacci series up to n terms

# input - take number of terms from user
n = int(input("Enter a number: "))

# computation - generate Fibonacci terms
def fib(n):
    if n == 0 or n == 1:
        return n            # base case: 0 or 1
    else:
        return fib(n - 1) + fib(n - 2)   # recursive case

# output - print Fibonacci series
print("Fibonacci Series:")
for i in range(n):
    print(fib(i), end=" ")

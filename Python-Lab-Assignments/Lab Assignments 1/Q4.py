# Program to swap two numbers without using third variable

a = int(input("Enter first number: "))  # input
b = int(input("Enter second number: "))  # input

a = a + b  # computation
b = a - b
a = a - b

print("After swapping, a =", a, "and b =", b)  # output

# Program to find largest and smallest of four numbers

a = int(input("Enter first number: "))  # input
b = int(input("Enter second number: "))  # input
c = int(input("Enter third number: "))  # input
d = int(input("Enter fourth number: "))  # input

largest = max(a, b, c, d)  # computation
smallest = min(a, b, c, d)  # computation

print("Largest number is", largest)  # output
print("Smallest number is", smallest)  # output

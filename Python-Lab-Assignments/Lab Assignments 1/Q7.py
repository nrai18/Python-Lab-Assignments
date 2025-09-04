# Program to find nature and roots of quadratic equation

a = float(input("Enter coefficient a: "))  # input
b = float(input("Enter coefficient b: "))  # input
c = float(input("Enter coefficient c: "))  # input

d = b**2 - 4*a*c  # computation

if d > 0:
    print("Roots are real and different")  # output
elif d == 0:
    print("Roots are real and equal")  # output
else:
    print("Roots are imaginary")  # output

if d >= 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("Roots are:", root1, "and", root2)  # output

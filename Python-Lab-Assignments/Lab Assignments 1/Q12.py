#Create a program to check the type of triangle (isosceles, equilateral, scalene).

# Input
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Computation: Check if it's a valid triangle
if a + b > c and b + c > a and a + c > b:
    
    # Check for equilateral
    if a == b and b == c:
        print("Equilateral triangle")
    
    # Check for isosceles
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    
    # Otherwise, it's scalene
    else:
        print("Scalene triangle")
else:
    # Not a valid triangle
    print("Not a triangle")

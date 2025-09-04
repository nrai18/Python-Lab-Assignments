# Program to check whether a number is even or odd

x = int(input("Enter a number: "))  # input

if (x & 1) == 1:  # computation
    print(str(x) + " is odd number")  # output
else:
    print(str(x) + " is even number")  # output

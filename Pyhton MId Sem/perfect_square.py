import math

# Function to check perfect square
def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n


# Main program
num = int(input("Enter a number: "))

if is_perfect_square(num):
    print(num, "is a Perfect Square")
else:
    print(num, "is NOT a Perfect Square")

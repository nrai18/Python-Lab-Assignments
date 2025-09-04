# Question 7b:Generate Geometric terms where first term is 1 and common ratio is 1⁄2.

# input - take number of terms from user
n = int(input("Enter a number: "))

# computation - generate Fibonacci terms
def geometric_series(i):
    if(n==0):
        return 1
    a=1
    R=1/2
    return a*R**i

# output - print Geometric series
print("Geometric Series :")
for i in range(n):
    print(geometric_series(i),end=" ")



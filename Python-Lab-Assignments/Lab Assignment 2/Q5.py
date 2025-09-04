# Question 5: Calculate value of e^x and sin(x) using series.
import math

# input - take x from user
x = float(input("Enter the value of x: "))
n = int(input("Enter number of terms for series: "))

# computation - calculate e^x using series
e_pow_x = 0
for i in range(n):
    e_pow_x += x**i / math.factorial(i)

# computation - calculate sin(x) using series
sin_x = 0
for i in range(n):
    sign = (-1)**i
    sin_x += sign * (x**(2*i + 1)) / math.factorial(2*i + 1)

# output - display e^x and sin(x)
print("e^x is:", e_pow_x)
print("sin(x) is:", sin_x)

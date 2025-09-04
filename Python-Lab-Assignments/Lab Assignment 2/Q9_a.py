# Question 9a: Find the sum of the series 1 + 3 + 5 + 7 + ...

# input - take number of terms from user
n = int(input("Enter the number of terms: "))

total_sum = 0
term = 1

# Loop 'n' times, adding each term to the sum
for i in range(n):
    total_sum += term
    term += 2

# output - print the final sum
print(f"The sum of the series is: {total_sum}")
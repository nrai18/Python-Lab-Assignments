# Question 9b: Find the sum of the series 1 - 1/2 + 1/3 - 1/4 + ...

# input - take number of terms from user
n = int(input("Enter the number of terms: "))

total_sum = 0.0

# Loop from 1 to n (inclusive) for each term
for i in range(1, n + 1):
    if i % 2 == 0:
        total_sum -= 1 / i
    else:
        total_sum += 1 / i

# output - print the final sum
print(f"The sum of the series is: {total_sum}")
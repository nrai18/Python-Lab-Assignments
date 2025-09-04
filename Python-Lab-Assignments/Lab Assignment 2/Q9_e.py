# Question 9e: Find the sum of the series 1³ + 2³ + 3³ + ...

# input - take number of terms from user
n = int(input("Enter the number of terms: "))

total_sum = 0

# Loop from 1 to n for each term in the series
for i in range(1, n + 1):
    # Calculate the cube of the term number and add it to the sum
    total_sum += i ** 3

# output - print the final sum
print(f"The sum of the series is: {total_sum}")

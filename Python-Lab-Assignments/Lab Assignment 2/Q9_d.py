# Question 9d: Find the sum of the series 1^2 - 2^2 + 3^2 - 4^2 + ...

# input - take number of terms from user
n = int(input("Enter the number of terms: "))

total_sum = 0

# Loop from 1 to n for each term in the series
for i in range(1, n + 1):
    # Calculate the value of the term, which is the square of the term number
    term = i ** 2
    
    # Check if the term number is even or odd to apply the correct sign
    if i % 2 == 0:
        total_sum -= term
    else:
        total_sum += term

# output - print the final sum
print(f"The sum of the series is: {total_sum}")
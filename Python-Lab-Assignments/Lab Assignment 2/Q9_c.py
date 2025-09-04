# Question 9c: Find the sum of the series 1! + 2! + 3! + 4! + ...

# input - take number of terms from user
n = int(input("Enter the number of terms: "))

total_sum = 0
factorial = 1

# Loop from 1 to n to calculate each term's factorial
for i in range(1, n + 1):
    # Calculate i! by multiplying the previous factorial (i-1)! with i
    factorial *= i
    
    # Add the current factorial to the total sum
    total_sum += factorial

# output - print the final sum
print(f"The sum of the series is: {total_sum}")
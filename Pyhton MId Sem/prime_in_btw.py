#(a) Write a Python program to print the prime numbers of up to a given number, accept the number from the user.

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Main program
n = int(input("Enter a number: "))

print(f"Prime numbers up to {n} are:")

for num in range(2, n + 1):
    if is_prime(num):
        print(num, end=" ")

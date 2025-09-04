# Question 6b: Check if number is prime.

# input - take number from user
n = int(input("Enter a number: "))

# condition - check for prime
if n < 2:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
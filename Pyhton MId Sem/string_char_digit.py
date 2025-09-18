#(b) Write a Python program to accepts a string and calculates the number of digits and letters.
# Function to count letters and digits without using isalpha or isdigit
def count_letters_digits(s):
    letters = 0
    digits = 0
    for ch in s:
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):  # check alphabet
            letters += 1
        elif '0' <= ch <= '9':  # check digit
            digits += 1
    return letters, digits


# Main program
text = input("Enter a string: ")
letters, digits = count_letters_digits(text)

print("Letters:", letters)
print("Digits:", digits)


# Function to count letters and digits
def count_letters_digits(s):
    letters = 0
    digits = 0
    for ch in s:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
    return letters, digits


# Main program
text = input("Enter a string: ")
letters, digits = count_letters_digits(text)

print("Letters:", letters)
print("Digits:", digits)

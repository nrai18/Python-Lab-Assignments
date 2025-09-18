# Function to check palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# Main program
text = input("Enter a string: ")

if is_palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is NOT a Palindrome")

# Program to display grade using if-else ladder

marks = int(input("Enter marks: "))  # input

if marks > 80:
    grade = "A"
elif marks >= 61:
    grade = "B"
elif marks >= 51:
    grade = "C"
elif marks >= 41:
    grade = "D"
elif marks >= 35:
    grade = "E"
else:
    grade = "F"

print("Grade is", grade)  # output

# Program to display grade using match-case

marks = int(input("Enter marks: "))  # input

match marks:
    case _ if marks > 80:
        print("Grade is A")
    case _ if marks >= 61:
        print("Grade is B")
    case _ if marks >= 51:
        print("Grade is C")
    case _ if marks >= 41:
        print("Grade is D")
    case _ if marks >= 35:
        print("Grade is E")
    case _:
        print("Grade is F")

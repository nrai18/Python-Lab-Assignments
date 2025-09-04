# Program to calculate simple and compound interest

p = float(input("Enter principal amount: "))  # input
r = float(input("Enter rate of interest: "))  # input
t = float(input("Enter time in years: "))  # input

si = (p * r * t) / 100  # computation
amount = p * (1 + r / 100) ** t
ci = amount - p  # computation

print("Simple Interest is:", si)  # output
print("Compound Interest is:", ci)  # output

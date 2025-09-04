# Convert total days into years, months, and days

days = int(input("Enter total number of days: "))  # input

years = days // 365  # computation
months = (days % 365) // 30
remaining_days = (days % 365) % 30

print("Years:", years, "Months:", months, "Days:", remaining_days)  # output

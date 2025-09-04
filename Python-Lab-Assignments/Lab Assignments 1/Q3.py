# Program to convert km to miles and miles to km

km_to_miles_factor = 0.621371
miles_to_km_factor = 1.60934

km = float(input("Enter the number of kilometers: "))  # input
miles = float(input("Enter the number of miles: "))    # input

km_in_miles = km * km_to_miles_factor  # computation
miles_in_km = miles * miles_to_km_factor  # computation

print(str(km) + " kilometers is equal to " + str(km_in_miles) + " miles.")  # output
print(str(miles) + " miles is equal to " + str(miles_in_km) + " kilometers.")  # output

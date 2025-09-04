# Convert seconds into hours, minutes, and seconds

seconds = int(input("Enter total seconds: "))  # input

hours = seconds // 3600  # computation
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("Hours:", hours, "Minutes:", minutes, "Seconds:", remaining_seconds)  # output
8
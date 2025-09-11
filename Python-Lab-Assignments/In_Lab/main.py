import os

filename = "file.txt"
with open(filename, "w") as f:
    f.write("Hello, this is the first line.\n")
print("File created and written successfully.\n")
with open(filename, "r") as f:
    content = f.read()
    print("Reading file content:\n")
    print(content)
with open(filename, "a") as f:
    f.write("This line is appended.\n")

print("\nData appended successfully.\n")

with open(filename, "r") as f:
    print("Reading file line by line:")
    for line in f:
        print(line.strip())


new_name = "new_file.txt"
os.rename(filename, new_name)
print(f"\nFile renamed to {new_name}")


if os.path.exists(new_name):
    print("Yes, the file exists.")

os.remove(new_name)
print(f"\nFile {new_name} deleted successfully.")

# Write a Python program to count the number of lines in a text file.

# initialising counter
count = 0

with open("textfile.txt", mode="r") as file:
    for line in file:
        print(line)
        count += 1

print(f"File has {count} lines")

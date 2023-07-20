# Write a Python program to read a file line by line and store it into a list.

lines = []
with open("textfile.txt", mode="r") as file:
    for line in file:
        lines.append(line)

print(lines)

# Write a Python program to read first n lines of a file.

n = 3
data = ""
with open("textfile.txt", mode="r") as file:
    for i in range(1, n):
        data += file.readline()

print(data)

# Write a Python program to read last n lines of a file.

n = 10
data = ""
with open("textfile.txt", mode="r") as file:
    # negative iterator
    for line in file.readlines()[-10:]:
        data += line

print(data)

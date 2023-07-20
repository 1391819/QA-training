# Write a Python program to read an entire text file
with open("textfile.txt", mode="r") as file:
    data = file.read()


print(data)

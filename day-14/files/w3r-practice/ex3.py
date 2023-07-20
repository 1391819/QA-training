# Write a Python program to append text to a file and display the text.

text = "I will append this\n"

with open("textfile.txt", mode="a") as file:
    file.write(text)

with open("textfile.txt", mode="r") as file:
    content = file.read()
    print(content)

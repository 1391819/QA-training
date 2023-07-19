# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# user input
word = input("Enter a word: ")
# can just use slicing to reverse the string
# [::-1] go through the entire string from end to start
reversed_word = word[::-1]

print(f"Original word is: {word}")
print(f"Reversed word is: {reversed_word}")

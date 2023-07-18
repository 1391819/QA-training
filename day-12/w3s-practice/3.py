# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# importing random lib
import random

# test for the while loop
guessed = False

# generating random number on program run
generated_number = random.randint(1, 10)

# while loop - do until guessed is True
while not guessed:
    # user input
    guess = int(input("Enter your guess: "))

    # check if user input is same as generated number
    if guess == generated_number:
        print("Well guessed!")
        guessed = True

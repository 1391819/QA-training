# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# creating original numbers list
original_numbers = [x for x in range(1500, 2701)]
valid_numbers = []

# going through all numbers
for number in original_numbers:
    # checking if the number is divisible by 7 and 5
    if (number % 7 == 0) and (number % 5 == 0):
        # appending if number is valid
        valid_numbers.append(number)

# print
print(valid_numbers)

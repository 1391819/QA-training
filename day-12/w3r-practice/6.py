# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# initialising counters
even_count = 0
odd_count = 0

# this could be turned into an user input
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# go through all numbers in the list
for number in numbers_list:
    # if even, increase even counter
    if number % 2 == 0:
        even_count += 1
    # else (if odd), increase odd counter
    else:
        odd_count += 1

# print number of odd and even numbers
print(f"Amount of even numbers in the list is {even_count}")
print(f"Amount of odd numbers in the list is {odd_count}")

# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# initialising counters
even_count = 0
odd_count = 0

# this could be turned into an user input
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers_list:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Amount of even numbers in the list is {even_count}")
print(f"Amount of odd numbers in the list is {odd_count}")

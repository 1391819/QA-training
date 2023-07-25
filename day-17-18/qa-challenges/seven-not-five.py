"""

Write a program to:

find all numbers, between 2000 and 3200 (both included), that are divisible by 7, but are not a multiple of 5
The numbers obtained should be returned on a single line. seperated by commas.

"""


def find_numbers(number_one, number_two, divisor, multiple):
    numbers = []

    for i in range(number_one, number_two + 1):
        if i % divisor == 0 and i % multiple != 0:
            numbers.append(str(i))

    return ", ".join(numbers)


if __name__ == "__main__":
    number_one = 2000
    number_two = 3200
    divisor = 7
    multiple = 5

    print(find_numbers(2000, 3200, 7, 5))

# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def print_even_numbers(numbers_list):
    even_numbers_list = []
    for number in numbers_list:
        if number % 2 == 0:
            even_numbers_list.append(number)

    print(f"Even numbers only: {even_numbers_list}")


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(numbers_list)

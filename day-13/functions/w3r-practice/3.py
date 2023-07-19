# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def mul_numbers(my_list):
    # the easy way I guess, without modules
    result = 1
    for number in my_list:
        result = result * number

    return result


numbers_list = [1, 2, 3, 4, 5]
mul = mul_numbers(numbers_list)
print(f"Mul is {mul}")

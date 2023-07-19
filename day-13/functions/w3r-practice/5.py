# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def compute_factorial(number):
    # factorial of 0 is 1
    if number == 0:
        return 1
    else:
        # multiply the number with the
        # factorial of n - 1
        return number * compute_factorial(number - 1)


number = 5
factorial = compute_factorial(number)
print(f"The factorial is {factorial}")

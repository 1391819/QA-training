# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def reverse_string(string):
    return string[::-1]


initial_string = "abcdefg"
reversed = reverse_string(initial_string)
print(f"Initial string: {initial_string}")
print(f"Reversed string: {reversed}")

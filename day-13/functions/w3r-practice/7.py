# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def count_upper_and_lower(string):
    upper_case_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lowercase_count += 1
        else:
            pass

    print(f"Uppercase count is: {upper_case_count}")
    print(f"Lowercase count is: {lowercase_count}")


count_upper_and_lower("The quick Brow Fox")

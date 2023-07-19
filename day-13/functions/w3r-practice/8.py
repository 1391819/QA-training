# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def get_unique_list(initial_list):
    # sets can't have duplicates
    # just use it
    return list(set(initial_list))


initial_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_unique_list(initial_list)


print(f"Initial list: {initial_list}")
print(f"Unique list: {unique_list}")

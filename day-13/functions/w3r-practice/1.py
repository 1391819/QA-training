# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def find_max(list):
    # max is going to be first item
    max = list[0]
    # then we need to compare it to the others
    for number in list:
        # if curr number is bigger
        if number > max:
            # assign max to curr number
            max = number
    return max


# numbers list declaration
numbers_list = [-76, -77, -78]
# calling function
max = find_max(numbers_list)
# printing
print(f"Max of numbers is: {max}")

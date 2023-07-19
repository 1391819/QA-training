# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def check_if_in_range(number, start, end):
    # + 1, just for logical purposes really
    # if number = 10, and given range is 5 - 10,
    # the number would be in range from a non-technical person
    # point of view
    if number in range(start, end + 1):
        return True

    return False


number = int(input("Enter number: "))
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

in_range = check_if_in_range(number, start, end)

if in_range:
    print(f"Number {number} is in range {start}-{end}")
else:
    print(f"Number {number} is not in range {start}-{end}")

# check if a number is palindrome or not
def is_palidrome(n):
    # can convert it to string, slice it, and return it
    n_string = str(n)
    n_string = n_string[::-1]
    reversed_n = int(n_string)

    if reversed_n == n:
        return True
    return False


# remove n chars from a given string
def remove_chars(s, n):
    return s[n:]


# calculate the cube of all numbers from 1 to the given number
def calculate_cubes(n):
    # will store cubes etc in here for now
    tmp_dict = {}

    # we include the given number
    for i in range(1, n + 1):
        cube = i**3
        tmp_dict[i] = cube

    return tmp_dict


if __name__ == "__main__":
    """
    # Check palindrome number
    n = 40
    isPalindrome = is_palidrome(n)
    print(f"Is number palindrome: {isPalindrome}")
    """
    # ------------------------------------------------------
    """
    # Remove first N chars from a string
    n = 3
    s = "testing this"
    new_s = remove_chars(s, n)
    print(f"Original string: {s}")
    print(f"Modified string: {new_s}")
    """
    # ------------------------------------------------------
    # Calculate the cube of all numbers from 1 to a given number
    n = 6
    cubes = calculate_cubes(n)

    for key, value in cubes.items():
        print(f"Cube of {key} is {value}")

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

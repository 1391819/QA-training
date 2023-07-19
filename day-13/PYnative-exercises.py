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
    # key is number
    # value is cube
    tmp_dict = {}

    # we include the given number
    for i in range(1, n + 1):
        cube = i**3
        tmp_dict[i] = cube

    return tmp_dict


# nested functions
# outer -> accept two parameters
# inner -> addition between two parameters
# outer -> add 5 to addition and return it
def outer_function(a, b):
    # parameters within the inner function can also be ommited
    # since they are global to everything within the outer function

    # this function is available within the outer faction now
    def inner_function():
        return a + b

    # we call the inner function from within the outer one
    sum = inner_function()

    # add 5 and return
    return sum + 5


# calculate sum of numbers
def recursive_function(n):
    # need to add check in order to not encounter
    # RecursionError: maximum recursion depth exceeded
    # could be done within a try catch block and handle it properly?
    # I'm not too familiar with recursive things
    if n:
        return n + recursive_function(n - 1)
    else:
        return 0


# create a new string made of the first, middle
# and last characters of each input string
def generate_string(s1, s2):
    # get lengths of strings - for the middle chars
    s1_len = len(s1)
    s2_len = len(s2)

    # get first chars
    first_chars = s1[0] + s2[0]
    # get middle chars
    middle_chars = (
        s1[int(s1_len / 2) : int(s1_len / 2) + 1]
        + s2[int(s2_len / 2) : int(s2_len / 2) + 1]
    )
    # get last chars
    last_chars = s1[-1] + s2[-1]

    return first_chars + middle_chars + last_chars


# arrange string chars such that lowercase letters
# come first
def arrange_string(s):
    # can also be done without using lists
    tmp_lower = []
    tmp_upper = []
    other_stuff = []

    # going through each char
    for char in s:
        if char.islower():
            tmp_lower.append(char)
        elif char.isupper():
            tmp_upper.append(char)
        else:
            other_stuff.append(char)

    # join lists
    final_string = "".join(tmp_lower + tmp_upper + other_stuff)

    return final_string


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

    """
    # Calculate the cube of all numbers from 1 to a given number
    n = 6
    cubes = calculate_cubes(n)

    # Go through returned dictionary
    for key, value in cubes.items():
        # Print key value pairs - number cube pairs
        print(f"Cube of {key} is {value}")

    """

    # ------------------------------------------------------

    """
    # Nested functions
    #
    # Create an inner function to calculate the addition
    # in the following way
    #
    # - Create an outer function that will accept two parameters, a and b
    # - Create an inner function inside an outer function that will calculate the addition of a and b
    # - At last, an outer function will add 5 into addition and return it
    a = 1
    b = 1
    # we just need to call the outer function to be fair
    addition = outer_function(a, b)
    print(f"Sum + 5 using nested functions is: {addition}")
    """

    # ------------------------------------------------------

    """
    # Recursive function
    #
    # Calculate the sum of numbers from 0 to n
    n = 10
    sum = recursive_function(n)
    print(f"Sum using recursive function is: {sum}")
    """

    # ------------------------------------------------------

    """
    # Strings
    #
    # Create a new string made of the first, middle, and
    # last characters of each input string
    s1 = "Roberto"
    s2 = "Nacu"
    final_s = generate_string(s1, s2)
    print(f"Original strings were {s1} and {s2}")
    print(f"Final string is: {final_s}")
    """

    # ------------------------------------------------------

    # Strings
    #
    # Arrange string characters such that lowercase letters
    # should come first
    s = "JKAHqwpidhqwdpkjd@#@[!bAAPSI23123HDUPA"
    arranged_s = arrange_string(s)
    print(f"Original string was: {s}")
    print(f"Arranged string is {arranged_s}")

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

    # ------------------------------------------------------

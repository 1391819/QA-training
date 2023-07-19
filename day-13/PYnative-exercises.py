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

    # Recursive function
    #
    # Calculate the sum of numbers from 0 to n
    n = 10
    sum = recursive_function(n)
    print(f"Sum using recursive function is: {sum}")

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

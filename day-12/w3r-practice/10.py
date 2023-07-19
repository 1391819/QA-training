# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php


# for loop 1 to 50
for i in range(1, 51):
    # if number is multiple of 3 and multiple of 5
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    # if number is multiple of 3
    elif i % 3 == 0:
        print("Fizz")
    # if number is multiple of 5
    elif i % 5 == 0:
        print("Buzz")
    # else just print the number
    else:
        print(f"Number is {i}")

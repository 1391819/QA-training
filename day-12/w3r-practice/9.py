# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# Fibonacci series between 0 and 50

# initialising numbers list
fibonacci_list = [0, 1]  # first two values

# just a big loop
while True:
    # calculating next number
    to_be_added = fibonacci_list[-1] + fibonacci_list[-2]
    # if greater than limit, we exit the loop
    if to_be_added >= 50:
        break
    # append next number to list
    fibonacci_list.append(to_be_added)


# printing all the fibonacci list
print(fibonacci_list)

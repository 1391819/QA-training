# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def check_if_prime(number):
    # 1 is not prime
    if number == 1:
        return False
    # 2 is always prime
    elif number == 2:
        return True
    else:
        # we need to check all its divisors
        for i in range(2, number):
            # if it has any divisors
            # it's not prime
            if number % i == 0:
                return False

        # else, the number's only divisors
        # are 1 and the number itself
        return True


number = int(input("Enter number: "))
is_prime = check_if_prime(number)

if is_prime:
    print(f"Number {number} is prime")
else:
    print(f"Number {number} is not prime")

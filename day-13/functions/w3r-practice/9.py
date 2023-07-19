# https://www.w3resource.com/python-exercises/python-functions-exercises.php


def check_if_prime(n):
    # 1 is not prime
    if n == 1:
        return False
    # 2 is always prime
    elif n == 2:
        return True
    else:
        # we need to check all its divisors
        for i in range(2, n):
            # if it has any divisors
            # it's not prime
            if n % i == 0:
                return False

        # else, the number's only divisors
        # are 1 and the number itself
        return True


n = int(input("Enter number: "))
is_prime = check_if_prime(n)

if is_prime:
    print(f"Number {n} is prime")
else:
    print(f"Number {n} is not prime")

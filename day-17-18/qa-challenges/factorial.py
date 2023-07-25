"""

Write a program which can compute the factorial of a given number.

The factorial of any given number is the multplication every whole number from our chosen one all the way down to 1.

"""


def fact(x):
    if x < 0:
        return None
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


if __name__ == "__main__":
    print(fact(0))
    print(fact(5))
    print(fact(8))
    print(fact(-1))

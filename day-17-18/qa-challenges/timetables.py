"""

Given an integer n, write a python function which returns a times table grid for all the integers between 1 and n.
The grid should be separated by tabs and new lines.

"""


def create_grid(n):
    grid = ""
    for i in range(1, n + 1):
        grid += "\t".join([str(x * i) for x in range(1, n + 1)]) + "\n"

    return grid


if __name__ == "__main__":
    n = 4
    print(create_grid(n))

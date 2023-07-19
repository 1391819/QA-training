def product(n):
    # from == to =, it's assignment
    total = 1

    # for loop
    for i in n:
        total *= i

    # return within function
    return total


print(product([4, 4, 5]))

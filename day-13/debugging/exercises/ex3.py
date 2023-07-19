# import pdb # debug


def is_prime(x):
    # pdb.set_trace()  # debug
    # 1 is not prime
    if x == 1:
        return False
    # 2 is
    if x == 2:
        return True
    else:
        for n in range(2, x - 1):
            # from = to ==, check, not assignment
            if x % n == 0:
                return False
        # moved outside for loop
        return True


print(is_prime(25))  # debug

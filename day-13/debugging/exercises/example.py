# A function to find the factorial of a number using tail recursion
def tail_recursion(factorial, result=1):
    if factorial == 1:
        return result
    else:
        # changed name, fixed factorial-- to factorial - 1
        return tail_recursion((factorial - 1), (factorial + result))

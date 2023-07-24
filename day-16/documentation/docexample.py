"""
	Multi-line comment
"""

# Single-line comment


class Example:
    """
    Example class docstring
    """

    def __init__(self) -> None:
        pass

    def factorial(x: int) -> int:
        """
        factorial(x): Returns the product of all of the integers from 1 to x inclusive
        More info here..
        """
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result


# called only when the module is called directly
if __name__ == "__main__":
    print(Example.factorial(3))  # 6
    print(Example.factorial(5))  # 120
    print(Example.factorial(10))  # big number

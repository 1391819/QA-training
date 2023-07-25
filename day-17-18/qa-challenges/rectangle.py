"""

Define a class named Rectangle, which can be constructed by a length and width.
The Rectangle class needs to have a method that can compute area.

"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width


if __name__ == "__main__":
    rectangle = Rectangle(10, 10)
    print(rectangle.compute_area())

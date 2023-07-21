# imports
from Shape import Shape


# Rectangle class
class Rectangle(Shape):
    # init
    def __init__(self, width, length):
        self.width = width  # width
        self.length = length  # length

    # return the area
    def get_area(self):
        return self.length * self.width

    # return the perimeter
    def get_perimeter(self):
        return (self.length * self.width) * 2

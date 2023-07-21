# imports
from Rectangle import Rectangle


# Square class
class Square(Rectangle):
    # init
    def __init__(self, width):
        # we call the init of the parent class Rectangle
        super().__init__(width, width)

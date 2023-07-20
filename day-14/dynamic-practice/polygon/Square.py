# imports
from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, width):
        # we call the init of the parent Class (Rectangle)
        super().__init__(width, width)

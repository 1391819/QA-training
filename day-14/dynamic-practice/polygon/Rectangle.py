from Shape import Shape


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length * self.width) * 2

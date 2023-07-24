"""

Create a Rectangle class which implements: 

    - an __init__ method which sets the rectangles height and width
    - a __str__ method which returns a string which is an ASCII-art drawing of the rectangle
    - an __int__ method which returns the rectangle's area
    
    Feel free to play around with implementing any of the other magic methods if you want to

"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self) -> str:
        vertical_char = "|"
        horizontal_char = "-"

        horizontal_line = []
        vertical_line = []

        for _ in range(self.width):
            horizontal_line.append(horizontal_char)

        # print(horizontal_line)  # debug

        for i in range(self.height):
            vertical_line.append("\n")

            for k in range(self.width):
                if k == 0 or k == self.width - 1:
                    vertical_line.append(vertical_char)
                else:
                    vertical_line.append(" ")

            if i == self.height - 1:
                vertical_line.append("\n")

        # print(vertical_line)  # debug

        horizontal_line = "".join(horizontal_line)
        vertical_line = "".join(vertical_line)

        ascii = horizontal_line + vertical_line + horizontal_line

        return ascii

    def __int__(self):
        """Return area of the rectangle

        Returns:
            int: Area of the rectangle
        """
        return self.width * self.height

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __add__(self, other_rectangle):
        return Rectangle(
            self.width + other_rectangle.width, self.height + other_rectangle.height
        )

    def __iadd__(self, other_rectangle):
        self.width += other_rectangle.width
        self.height += other_rectangle.height
        return self

    def __sub__(self, other_rectangle):
        return Rectangle(
            self.width - other_rectangle.width
            if other_rectangle.width > self.width
            else self.width,
            self.height - other_rectangle.height
            if other_rectangle.height > self.height
            else self.height,
        )

    def __isub__(self, other_rectangle):
        self.width -= other_rectangle.width
        self.height -= other_rectangle.height
        return self


if __name__ == "__main__":
    # creating rectangles
    rectangle1 = Rectangle(20, 10)
    rectangle2 = Rectangle(20, 30)

    # printing rectangle1 - ASCII art
    print(rectangle1)

    # converting to int (calculating area)
    print(int(rectangle1))

    print(rectangle1 + rectangle2)

    print(rectangle2 - rectangle1)

    rectangle1 += rectangle2
    print("Addition + assignment done - overwritten")
    print(f"Rectangle1 width {rectangle1.width} and height {rectangle1.height}")
    rectangle2 -= rectangle1
    print("Subtraction + assignment done - overwritten")
    print(f"Rectangle2 width {rectangle2.width} and height {rectangle2.height}")

    # print(f"Eval: {eval(rectangle1.__repr__())}")

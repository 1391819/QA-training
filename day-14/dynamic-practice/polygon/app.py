"""

Goal:

Create class and sub-class objects which represent different geometrical shapes, such as Rectangles and Squares.
Objects should have methods to display area and perimeter.

"""

# imports
from Square import Square
from Rectangle import Rectangle

# main
if __name__ == "__main__":
    # creating Square and Rectangle instances
    square1 = Square(5)
    rectangle1 = Rectangle(7, 10)

    # printing area and perimeter of the square
    print(f"Area of the square is {square1.get_area()}")
    print(f"Perimeter of the square is {square1.get_perimeter()}")

    # printing area and perimeter of the rectangle
    print(f"Area of the rectangle is {rectangle1.get_area()}")
    print(f"Perimeter of the rectangle is {rectangle1.get_perimeter()}")

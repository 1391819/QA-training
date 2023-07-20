from Square import Square
from Rectangle import Rectangle

if __name__ == "__main__":
    square1 = Square(5)
    rectangle1 = Rectangle(7, 10)

    print(f"Area of the square is {square1.get_area()}")
    print(f"Perimeter of the square is {square1.get_perimeter()}")

    print(f"Area of the rectangle is {rectangle1.get_area()}")
    print(f"Perimeter of the rectangle is {rectangle1.get_perimeter()}")

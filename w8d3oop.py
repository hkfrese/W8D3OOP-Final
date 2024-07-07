from math import pi, sqrt

class Shape:
    def __init__(self, color): #Constructor to initialize the shape with the given color.
        self._color = color

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_perimeter(self): # method to calculate the perimeter of the shape.
        raise NotImplementedError("Subclasses must implement this method")

    def get_color(self): #retrieve the color of the shape.
        return self._color

    def set_color(self, color): #set the color of the shape.
        self._color = color

class Circle(Shape):
    def __init__(self, color, radius): #initialize the circle with the given color and radius
        super().__init__(color)
        self._radius = radius

    def calculate_area(self): #calculate the area of the circle
        return pi * (self._radius ** 2)

    def calculate_perimeter(self): #calculate the perimeter (circumference) of the circle
        return 2 * pi * self._radius

class Rectangle(Shape):
    def __init__(self, color, length, width): #initialize the rectangle with the given color, length, and width.
        super().__init__(color)
        self._length = length
        self._width = width

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2 * (self._length + self._width)

class Triangle(Shape):
    def __init__(self, color, side1, side2, side3): #initialize the triangle with the given color and side lengths.
        super().__init__(color)
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def calculate_area(self):
        s = (self._side1 + self._side2 + self._side3) / 2
        return sqrt(s * (s - self._side1) * (s - self._side2) * (s - self._side3))

    def calculate_perimeter(self):
        return self._side1 + self._side2 + self._side3

def main():
    # Create instances of different shapes
    shapes = [
        Circle("Red", 5),
        Rectangle("Blue", 4, 6),
        Triangle("Green", 3, 4, 5)
    ]

    # Iterate over the list of shapes and display their details
    for shape in shapes:
        print(f"Shape: {shape.__class__.__name__}")
        print(f"Color: {shape.get_color()}")
        print(f"Area: {shape.calculate_area()}")
        print(f"Perimeter: {shape.calculate_perimeter()}")
        print()

if __name__ == "__main__":
    main()
# W8D3OOP-Final
# W8D3OOP
# W8D3OOP ##ChatGPT helped me write the documentation for this since there was a lot to cover. 
Shape Classes
This class represents various geometric shapes, allowing for the calculation of their areas and perimeters, while also providing a common interface for setting and getting their colors.

Classes:
Shape:

Attributes:
_color (string): The color of the shape.
Methods:
__init__(self, color): Initializes the shape with the given color.
calculate_area(self): method to calculate the area of the shape.
calculate_perimeter(self): method to calculate the perimeter of the shape.
get_color(self): Retrieves the color of the shape.
set_color(self, color): Sets the color of the shape.

Circle (inherits from Shape):
Attributes:
_radius (float): The radius of the circle.
Methods:
__init__(self, color, radius): Initializes the circle with the given color and radius.
calculate_area(self): Calculates the area of the circle (πr²).
calculate_perimeter(self): Calculates the perimeter (circumference) of the circle (2πr).
Rectangle (inherits from Shape):

Attributes:
_length (float): The length of the rectangle.
_width (float): The width of the rectangle.
Methods:
__init__(self, color, length, width): Initializes the rectangle with the given color, length, and width.
calculate_area(self): Calculates the area of the rectangle (length * width).
calculate_perimeter(self): Calculates the perimeter of the rectangle (2 * (length + width)).
Triangle (inherits from Shape):

Attributes:
_side1 (float): The length of the first side of the triangle.
_side2 (float): The length of the second side of the triangle.
_side3 (float): The length of the third side of the triangle.
Methods:
__init__(self, color, side1, side2, side3): Initializes the triangle with the given color and side lengths.
calculate_area(self): Calculates the area of the triangle using Heron's formula.
calculate_perimeter(self): Calculates the perimeter of the triangle (side1 + side2 + side3).

To Run the Program
Run the program by executing w9d3oop.py# W8D3OOP
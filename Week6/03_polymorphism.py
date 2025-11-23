"""
Week 6: Polymorphism Examples
Topics: Method overriding, duck typing
"""

class Shape:
    """Base class for shapes"""
    
    def area(self):
        pass
    
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Polymorphism in action
def print_shape_info(shape):
    """Works with any shape object"""
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")


print("=== Polymorphism ===")
rect = Rectangle(5, 3)
circle = Circle(7)

print("Rectangle:")
print_shape_info(rect)

print("\nCircle:")
print_shape_info(circle)

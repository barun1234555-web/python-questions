import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2  # Semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

tri = Triangle(3, 4, 5)
print(f"Area: {tri.area()}, Perimeter: {tri.perimeter()}")
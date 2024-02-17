from abc import ABC, abstractmethod
import copy

class Forma(ABC):
    @abstractmethod
    def clone(self):
        pass

class Circle(Forma):
    def __init__(self, color, ray):
        self.color = color
        self.ray = ray

    def clone(self):
        return copy.deepcopy(self)

class Rectangle(Forma):
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

class triangle(Forma):
    def __init__(self, color, lado1, lado2, lado3):
        self.color = color
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def clone(self):
        return copy.deepcopy(self)

Circle_original = Circle("red", 5)
copia_Circle = Circle_original.clone()
print("Cópia do círculo - cor:", copia_Circle.color, "ray:", copia_Circle.ray)

Rectangle_original = Rectangle("blue", 10, 5)
copia_Rectangle = Rectangle_original.clone()
print("Cópia do retângulo - cor:", copia_Rectangle.color, "width:", copia_Rectangle.width, "height:", copia_Rectangle.height)

triangle_original = triangle("green", 3, 4, 5)
copia_triangle = triangle_original.clone()
print("Cópia do triângulo - cor:", copia_triangle.color, "Lados:", copia_triangle.lado1, copia_triangle.lado2, copia_triangle.lado3)

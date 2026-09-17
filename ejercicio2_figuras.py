import math

class Figura:
    def area(self):
        return 0

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

# Prueba
rectangulo = Rectangulo(6, 5)
circulo = Circulo(5)
triangulo = Triangulo(7, 5)

print(f"Área del rectángulo: {rectangulo.area()}")
print(f"Área del círculo: {circulo.area()}")
print(f"Área del triángulo: {triangulo.area()}")

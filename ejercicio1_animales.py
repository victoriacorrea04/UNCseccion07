class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print(" 🐶 ¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(" 🐱 ¡Miau miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print(" 🐮 ¡Muuuu!")

class Caballo(Animal):
    def hacer_sonido(self):
        print(" 🐴 ¡Hiiiiieee!")        

# Prueba
animales = [Perro("Eros", 7), 
            Gato("Noah", 5), 
            Vaca("Mancha", 10), 
            Caballo("Blue jeans", 15)
]

for animal in animales:
    print(f"{animal.nombre} ({animal.edad} años): ", end="")
    animal.hacer_sonido()

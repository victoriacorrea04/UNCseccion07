class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.__salario_base = salario_base

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario_base = nuevo_salario
        else:
            print("El salario debe ser positivo")

    def calcular_salario(self):
        return self.__salario_base

class Gerente(Empleado):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self._Empleado__salario_base = salario_base

    def calcular_salario(self):
        bono = self._Empleado__salario_base * 0.30
        return self._Empleado__salario_base + bono

class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas):
        self.nombre = nombre
        self._Empleado__salario_base = salario_base
        self.ventas = ventas

    def calcular_salario(self):
        comision = self.ventas * 0.10
        return self._Empleado__salario_base + comision

# Prueba
empleados = [
    Empleado("Victoria ♌ ", 7000),
    Gerente("Daniela ♉ ", 9000),
    Vendedor("Laura ♏ ", 2500, 5000)
]

for empleado in empleados:
    print(f"{empleado.nombre} gana: ${empleado.calcular_salario()}")

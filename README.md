# ***Práctica #6 – Enunciados:*** 
___
### ***#1*** Desarrolle una clase base denominada "Animal" que incluya los atributos "nombre" y "edad", junto con un método "hacer_sonido()" que emita un mensaje genérico. Posteriormente, implemente tres clases derivadas: 

Perro ("¡Guau guau!")  

Gato ("¡Miau miau!") 

Vaca ("¡Muuuu!"). 

*Requisitos: cada clase hija debe sobrescribir el método "hacer_sonido()" y se debe iterar sobre una lista conteniendo un objeto de cada tipo para ejecutar dicho método.*

 ### ***#2*** Implemente una clase base "Figura" con un método "area()" que retorne 0. Defina las clases hijas: Rectángulo (base y altura), Círculo (radio, utilizando math.pi) y Triángulo (base y altura). 
 
 *Requisitos: todas las figuras deben heredar de la clase base, almacenarse en una lista y mostrar su área calculada.*

 ### ***#3*** Cree una clase base "Empleado" con los atributos "nombre" y "salario_base", incluyendo un método "calcular_salario()". Defina las clases hijas: Gerente (salario base más 30% de bono) y Vendedor (salario base más 10% de comisión sobre ventas).
 
 *Requisitos: utilice "super()._init_()" en las clases derivadas y presente el salario de cada empleado registrado en una lista.*
___

# ***PRUEBA #2 (Enunciados)***

### ***Enunciado 3: Brazos Robóticos***

Descripción:
Clase base BrazoRobotico con:
• Atributo privado __modelo
• Atributo protegido _grados_libertad
• Método mover() -> "El brazo se mueve".

Clases hijas:
• BrazoArticulado -> sobrescribe mover() -> "💪 Brazo articulado moviéndose en 6 ejes".
• BrazoCartesiano -> sobrescribe mover() -> "📐 Brazo cartesiano moviéndose en X, Y, Z".

Requisitos:
• Usa @property para el modelo.
• Usa super().__init__() en las hijas.
• Crea un objeto de cada clase y llama a mover().

###  ***Enunciado 7: Sistemas de Visión***

Descripción:
Clase base Camara con:
• Atributo privado __resolucion
• Atributo protegido _encendida (inicia en False)
• Método capturar() -> "Capturando imagen genérica".

Clases hijas:
• CamaraRGB -> sobrescribe capturar() -> "📷 Capturando imagen a color".
• CamaraInfrarroja -> sobrescribe capturar() -> "📉 Capturando imagen térmica".

Requisitos:
• Encapsula la resolución con @property.
• Crea un objeto de cada clase y llama a capturar().

### ***Enunciado 10: Robots de Soldadura***

Descripción:
Clase base RobotSoldador con:
• Atributo privado __modelo
• Atributo protegido _temperatura
• Método soldar() -> "El robot suelda una pieza".

Clases hijas:
• SoldadorPunto -> sobrescribe soldar() -> "⚡ Soldando por puntos".
• SoldadorArco -> sobrescribe soldar() -> "🔥 Soldando por arco eléctrico".

Requisitos:
• Encapsula el modelo con @property.
• Usa super().__init__() en las hijas.
• Crea un objeto de cada clase y llama a soldar().


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

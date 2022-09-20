# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:58:25 2022
@course: Curso de Python Cientifico, version 1.0
@author: Hugo Perez
@description: executable program
"""

#!/usr/bin/python
#-*- coding: utf-8 -*-

# Mensaje de Bienvenida
print("Programa de calculo del cubo de un numero.\n")

# Paso 2: Definimos una funcion que calcula el cubo de un numero cualquiera
def cubo(x):    
    # Calculo el valor del cubo de x
    y = x**3
    return y


# Numero de entrada
# x = input('Dame un numero: ')
# x = float(x)

# Paso 3: EL primer elelemnto es el nombre del programa 
# y el segundo el primer parametro
x = input("Ingrese el valor: ")
x = float(x)

#Imprimo el resultado
resultado = cubo(x)
# print("El cubo de %.2f es %.2f" % (x, resultado))
# Otra forma de presentar el resultado, usando format
print("El cubo dse {} es {}".format(x, resultado))

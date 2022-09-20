#!/usr/bin/python
#--*-- coding: utf-8 -*-

"""Programa de calculo del cubo de un numero"""

__author__ = "Jorge"
__copyright__ = "Curso de Python"
__credits__ = ["Pepe", "José Luis", "Roberto"]
__licence__ = "GPL"
__version__ = "1.0"
__email__ = "japp@denebola.org"
__status__ = "Development"

def cubo(x):
    """Calcula el cubo de un numero"""
    y = x**3
    return y

if __name__=="__main__":
    x = int(input("Dame un mumero: "))
    y = cubo(x)
    print("El cubo de %.2f es %.2f" % (x, y))
    

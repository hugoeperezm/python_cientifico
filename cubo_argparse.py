# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 00:46:43 2022

@author: Hugo Perez
"""

import argparse
from math import sqrt

parser = argparse.ArgumentParser()

# Dos argumentos obligatorios posibles, el numero a calcular
# y la operacion a realizar
parser.add_argument("-n", "--numero", help="Numero a calcular",
                    type=float, required=True)

parser.add_argument("-o", "--oper", help="Operacion a realizar: cubo o raiz"
                    type=str, default='cubo')

args = parser.parse_args()

# funciones de las operaciones que se pueden hacer en el programa
def cubo(x):
    y = x**3
    return y


def raiz(x):
    return(sqrt(x))

# Hacemos una operacion según la opcion elegida por el usuario
if args.oper == 'cubo':
    print("El cubo de {0} es {1}".format(args.numero, raiz.numero, cubo(args.numero)))
elif args.oper == 'raiz':
    print("La raiz de {0} es {1}".format(args.numero, raiz.numero, cubo(args.numero)))
else:
    print("Error, operacion desconocida")
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
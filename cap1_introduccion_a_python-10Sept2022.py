# IPython log file

get_ipython().run_line_magic('pwd', '')
#[Out]# 'D:\\Drive\\OneDrive - ULTRACOM IT SAS\\Proyectos\\Hugo\\CIENCIA-Python'
113/27
#[Out]# 4.185185185185185
frase = "Esta es una linea de texto"
num = 22
num*2
#[Out]# 44
frase*2
#[Out]# 'Esta es una linea de textoEsta es una linea de texto'
complejo = 1.2 + 5.0j # complex(1.2, 5.0)
type(complejo)
#[Out]# complex
print(complejo)
print(round(4.4)), (round(4.5))
#[Out]# (None, 4)
print(round(4.4), (round(4.5))

)
print(round(4.4)), (round(4.5))
#[Out]# (None, 4)
valor = input("Ingrese un numero: ")
type(valor) == int
#[Out]# False
frase = "Si he logrado ver mas lejos, ha sido porque he subido a hombros de gigantes"
print(frase[68:]
)
print(frase[:10]
)
print(frase[len(frase)-1])
print(frase[-1])
print(frase[-1] == frase[len(frase)-1])
type(frase)
#[Out]# str
dir(frase)
#[Out]# ['__add__',
#[Out]#  '__class__',
#[Out]#  '__contains__',
#[Out]#  '__delattr__',
#[Out]#  '__dir__',
#[Out]#  '__doc__',
#[Out]#  '__eq__',
#[Out]#  '__format__',
#[Out]#  '__ge__',
#[Out]#  '__getattribute__',
#[Out]#  '__getitem__',
#[Out]#  '__getnewargs__',
#[Out]#  '__gt__',
#[Out]#  '__hash__',
#[Out]#  '__init__',
#[Out]#  '__init_subclass__',
#[Out]#  '__iter__',
#[Out]#  '__le__',
#[Out]#  '__len__',
#[Out]#  '__lt__',
#[Out]#  '__mod__',
#[Out]#  '__mul__',
#[Out]#  '__ne__',
#[Out]#  '__new__',
#[Out]#  '__reduce__',
#[Out]#  '__reduce_ex__',
#[Out]#  '__repr__',
#[Out]#  '__rmod__',
#[Out]#  '__rmul__',
#[Out]#  '__setattr__',
#[Out]#  '__sizeof__',
#[Out]#  '__str__',
#[Out]#  '__subclasshook__',
#[Out]#  'capitalize',
#[Out]#  'casefold',
#[Out]#  'center',
#[Out]#  'count',
#[Out]#  'encode',
#[Out]#  'endswith',
#[Out]#  'expandtabs',
#[Out]#  'find',
#[Out]#  'format',
#[Out]#  'format_map',
#[Out]#  'index',
#[Out]#  'isalnum',
#[Out]#  'isalpha',
#[Out]#  'isascii',
#[Out]#  'isdecimal',
#[Out]#  'isdigit',
#[Out]#  'isidentifier',
#[Out]#  'islower',
#[Out]#  'isnumeric',
#[Out]#  'isprintable',
#[Out]#  'isspace',
#[Out]#  'istitle',
#[Out]#  'isupper',
#[Out]#  'join',
#[Out]#  'ljust',
#[Out]#  'lower',
#[Out]#  'lstrip',
#[Out]#  'maketrans',
#[Out]#  'partition',
#[Out]#  'removeprefix',
#[Out]#  'removesuffix',
#[Out]#  'replace',
#[Out]#  'rfind',
#[Out]#  'rindex',
#[Out]#  'rjust',
#[Out]#  'rpartition',
#[Out]#  'rsplit',
#[Out]#  'rstrip',
#[Out]#  'split',
#[Out]#  'splitlines',
#[Out]#  'startswith',
#[Out]#  'strip',
#[Out]#  'swapcase',
#[Out]#  'title',
#[Out]#  'translate',
#[Out]#  'upper',
#[Out]#  'zfill']
frase.capitalize()
#[Out]# 'Si he logrado ver mas lejos, ha sido porque he subido a hombros de gigantes'
frase.upper()
#[Out]# 'SI HE LOGRADO VER MAS LEJOS, HA SIDO PORQUE HE SUBIDO A HOMBROS DE GIGANTES'
frase
#[Out]# 'Si he logrado ver mas lejos, ha sido porque he subido a hombros de gigantes'
num
#[Out]# 22
type(num)
#[Out]# int
print("%.50f" % log10(2.0**100))
print("%.50f" % log10(2.0**100))
import math
print("%.50f" % math.log10(2.0**100))
print("El %s de %d es %f." % ('cubo', 10, 10.**3)
)
print("El %s de %d es %f." % ('cubo', 10, 10.**3))
print("El %s de %d es %10.5f." % ('cubo', 10, 10.**3))
print("El %s de %d es %10.2f." % ('cubo', 10, 10.**3))
print("El %s de %d es %6.2f." % ('cubo', 10, 10.**3))
resultado = format(0.0003567,".5e")
resultado
#[Out]# '3.56700e-04'
# resultado de un calculo obtenido con las cifras
# decimales que proporciona el ordenador
resultado = 3.1415785439847501
# este es un error con igual numero de cifras decimales
error = 0.0001345610900435
# asi expresamos de forma correcta el resultado
print("El resultado del experimento es %.4f +/- %.4f" ) % (resultado, error)
print("El resultado del experimento es %.4f +/- %.4f" % (resultado, error))
print("{:.2f}".format(3.1415926))
resultado = "El {operacion} de {numero} es {resultado}".format(operacion = "cubo", numero=7, resultado = 7**3)
print(resultado)
# Estructura de datos
estrellas ["alhena", "Mizar", "Cor Caroli", "Nunki", "Sadr"]
estrellas = ["alhena", "Mizar", "Cor Caroli", "Nunki", "Sadr"]
datos = ["Beta pictoris", 1.6, [1, 2, -3]]
palabras = frase.split()
print(palabras)
estrellas[-1]
#[Out]# 'Sadr'
estrellas
#[Out]# ['alhena', 'Mizar', 'Cor Caroli', 'Nunki', 'Sadr']
estrellas[1:3]
#[Out]# ['Mizar', 'Cor Caroli']
# Iterador de enteros de 0 a 4
list(range(5))
#[Out]# [0, 1, 2, 3, 4]
list(range(10, 16))
#[Out]# [10, 11, 12, 13, 14, 15]
# Lista de enteros de 10 a 20 de dos en dos
list(range(10, 20, 2))
#[Out]# [10, 12, 14, 16, 18]
estrellas.append()
estrellas.append(34)
estrellas
#[Out]# ['alhena', 'Mizar', 'Cor Caroli', 'Nunki', 'Sadr', 34]
estrellas.insert(3, "hamal")
estrellas
#[Out]# ['alhena', 'Mizar', 'Cor Caroli', 'hamal', 'Nunki', 'Sadr', 34]
estrellas.
c = (1, 3)
type(c)
#[Out]# tuple
parametros = 4, 5, 2, -1, 0
type(parametros)
#[Out]# tuple
estrellas = set(("Alhena", "Mizar", "Cor Caroli"))
estrellas1 = set(("Alhena", "Mizar", "Cor Caroli"))
estrellas2 = set(("Mizar", "Cor Caroli", "Nunki", "Sadr"))
"Alhena" in estrella1
"Alhena" in estrellas1
#[Out]# True
"Alhena" in estrellas2
#[Out]# False
# Union 
estrellas1 | estrellas2
#[Out]# {'Alhena', 'Cor Caroli', 'Mizar', 'Nunki', 'Sadr'}
estrellas1 & estrellas2
#[Out]# {'Cor Caroli', 'Mizar'}
estrellas1 - estrellas2
#[Out]# {'Alhena'}
estrellas1 ^ estrellas2
#[Out]# {'Alhena', 'Nunki', 'Sadr'}
import math
print math.sin(0.5*math.pi)
print( math.sin(0.5*math.pi))
dir(math)
#[Out]# ['__doc__',
#[Out]#  '__loader__',
#[Out]#  '__name__',
#[Out]#  '__package__',
#[Out]#  '__spec__',
#[Out]#  'acos',
#[Out]#  'acosh',
#[Out]#  'asin',
#[Out]#  'asinh',
#[Out]#  'atan',
#[Out]#  'atan2',
#[Out]#  'atanh',
#[Out]#  'ceil',
#[Out]#  'comb',
#[Out]#  'copysign',
#[Out]#  'cos',
#[Out]#  'cosh',
#[Out]#  'degrees',
#[Out]#  'dist',
#[Out]#  'e',
#[Out]#  'erf',
#[Out]#  'erfc',
#[Out]#  'exp',
#[Out]#  'expm1',
#[Out]#  'fabs',
#[Out]#  'factorial',
#[Out]#  'floor',
#[Out]#  'fmod',
#[Out]#  'frexp',
#[Out]#  'fsum',
#[Out]#  'gamma',
#[Out]#  'gcd',
#[Out]#  'hypot',
#[Out]#  'inf',
#[Out]#  'isclose',
#[Out]#  'isfinite',
#[Out]#  'isinf',
#[Out]#  'isnan',
#[Out]#  'isqrt',
#[Out]#  'lcm',
#[Out]#  'ldexp',
#[Out]#  'lgamma',
#[Out]#  'log',
#[Out]#  'log10',
#[Out]#  'log1p',
#[Out]#  'log2',
#[Out]#  'modf',
#[Out]#  'nan',
#[Out]#  'nextafter',
#[Out]#  'perm',
#[Out]#  'pi',
#[Out]#  'pow',
#[Out]#  'prod',
#[Out]#  'radians',
#[Out]#  'remainder',
#[Out]#  'sin',
#[Out]#  'sinh',
#[Out]#  'sqrt',
#[Out]#  'tan',
#[Out]#  'tanh',
#[Out]#  'tau',
#[Out]#  'trunc',
#[Out]#  'ulp']
a, b = 4.4, 4.5
print(math.ceil(a)), (math.ceil(b))
#[Out]# (None, 5)
print(math.ceil(a), math.ceil(b))
print(math.floor(a), math.floor(b))
math.floor.help()
math.help()
help(math)
help(math.floor)

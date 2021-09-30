'''
obtener las ventas de tres dias y mostrar el promedio
desarrollar una funcion que calcule el promedio
y retorne el resultado limitado a dos decimales

--> el promedio de los dats ingresados es:
'''

#solucion ejercicio

def promedio(a:int,b:int,c:int)->float:
    prom = (a+b+c) / 3
    return round(prom, 2)

a = int(input("ingrese ventas del dia 1 "))
b = int(input("ingrese ventas del dia 2 "))
c = int(input("ingrese ventas del dia 3 "))

result = promedio(a,b,c)
print("el promedio nde los datos ingresados es {}".format(result))




'''
desarrolle un algoritmo que pida por consola
al usuario un numero. este numero debe mostrarselo
codificado con la siguiente formula:
---> (dato * numero_aleatorio) ** numero_aleatorio
los numeros aleatorios para la formula son entre 1 y 500.
para este fin usted debe desarrrollar una funcion la cual
tenga como finalidad codificar cualquier valor con la formula dada
'''


#solucion
import random
#contruir la funcion

def codificar(number: int):
    #pedir valor al usuario
    number: int = int( input("por favor ingrese el numero  a codificar: "))
    rand = random.randint(1,500)
    resultado = (number * rand) ** rand
    return resultado



num_codificado: int = codificar
print("el numero codificado es{}".format(num_codificado))

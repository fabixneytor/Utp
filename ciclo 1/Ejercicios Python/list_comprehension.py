
#print([ x for x in range(0,31) if x%2==0 ])

mi_diccionario = dict()
for y in range(3, 11):
    mi_diccionario[(y, y**3)] = []
    for x in range(4, 31, 2):
        if x%y == 0:
            mi_diccionario[(y, y**3)].append(x**2)

#print(mi_diccionario)

mi_diccionario = { (x, x**3) : [ y**2 for y in range(4,31,2) if y%x == 0 ] for x in range(3,11) }
#print(mi_diccionario)


"""
cree un diccionario donde sus claves son tuplas de numeros
entre 1 y 100, el primer elemento de la tupla es el incrementable
y el segundo debe de estar elevado al cuadrado.
el valor del diccionario debe ser valores aleatorios pares entre 1 y 1000.
crear y mostrar el diccionario en una sola linea de codigo
"""

import random as r

#print({(x, x**2): [y for y in range(1, r.randint(1,1000)) if y%2==0] for x in range(1,101) })


"""
ejercicio 2:
crear dos conjuntos con valores aleatorios entre 1 y 1000 en una iteracion de 0 a 400.
mostrar los valores en comun que tienen los dos conjuntos
"""

conjunto_1 = { r.randint(1,100) for x in range(0,400)}
conjunto_2 = { r.randint(1,100) for x in range(0,400)}

print("Conjunto 1--->  ", conjunto_1)
print("Conjunto 2--->  ", conjunto_2)
print( conjunto_1.intersection(conjunto_2))
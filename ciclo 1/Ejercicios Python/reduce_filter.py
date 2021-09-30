

#funcion a aplicar en el filter, retorna un booleano
def menores_10(numero):
    return numero < 10

#lista a aplicar el filter
lista: list = [1,2,3,4,10,11,12,14,15,16]

#funcion para aplicar sobre el filter (numeros menores o iguales a 10)
funcion_lambda =  lambda numero: True if numero < 10 else False
#aplica un filter sobre la lista
resultado =  list( filter(funcion_lambda, lista ))
print( resultado )


'''
Desarrolle un programa que reciba como parametro una lista de peliculas y un caracter.
Retorne una nueva lista con las peliculas que empiezan con el caracter que recibe como parametro
'''

pelicula1 = ["Mi villano favorito", "El castigador", "El principe de persia",
            "El paseo 5", "Busqueda implacable"]

pelicula2 = ["Kung fu panda", "El hombre de acero", "Buscando a nemo", "Bella eres"]

pelicula3 = ["Mi pobre angelito", "Mamá quien dispara", "La gran estafa"]


def names_letters(x):
    return 'E' == x[0] #x[0].lower() in 'mb'

filtered_names = filter(names_letters, pelicula1)

print(list(filtered_names))

print("------------REDUCE-------------")
from functools import reduce
#lista de numeros del 1 al 100
lista: list = [ x for x in range(0,100)]
#funcion anonima encargada de realizar una suma
func_suma = lambda acumulador = 0, elemento = 0: (acumulador+elemento)
#aplicamos un reduce sobre la lista de elementos ( se sumaran todos)
resultado = reduce(func_suma, lista)
print(resultado)

print("---------CONCATENAR CON REDUCE-----------")

"""
Obtener a partir de una lista que almacene las ventas
de un almacen, un string de la siguiente manera:
$20000, $10000, $30000, .....
"""

#creo mi lista con valores en miles
mi_lista = [x*1000 for x in range(1,10)]
#creo una funcion anonima para concatenar los valores con $valor, $otro_valor,...
func_concatenar = lambda concatenador = "", elemento = "": concatenador+" , $"+elemento
#aplico el reduce para obtener un string de los eñementos numericos y
#finalmente los muestro en pantalla
print( "$", reduce(func_concatenar, list(map(lambda numero: str(numero), mi_lista))))
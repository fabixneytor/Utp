
funcion_suma = lambda val1, val2, val3 : (val1+val2+val3)/3
#primer llamado de la funcion lambda
print(funcion_suma(40,50,10))

#segundo llamado de la funcion lambda
print(funcion_suma(10,10,10))

#creacion de listas
crear_lista = lambda inicio,final : [ x for x in range(inicio, final)]

lista1 = crear_lista(5,10)
print(lista1)

lista2 = crear_lista(30,61)
print(lista2)


#castear lista de numeros a string
numeros: list = [1,2,3,4,5,6,7,8,9]
castear = lambda numeros: [str(x) for x in numeros]

print( ''.join(castear(numeros)))

#diccionario
diccionario = {
    'a' : 10,
    'b' : 20,
    'c' : 30
}

lambda_diccionario = lambda **diccionario: print(diccionario)

lambda_diccionario(diccionario)


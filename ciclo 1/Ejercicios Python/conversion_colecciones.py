

mensaje = "Hola Mundo"
print(mensaje)

#convertir cadena a lista

lista: list = list(mensaje)
lista[0] = 'J'
print(lista)

#Convertir a string
print( ''.join(lista))

#string a tuplas
tupla: tuple = tuple(mensaje)
print(tupla)

#tuplas de tuplas
cadena2 = 'colombia'
tupla2: tuple = tuple(cadena2)
tupla_general: tuple = (tupla, tupla2)
print(tupla_general)
print(tupla_general[0])

tupla = (1,2,3)
print(tupla)
var1, var2, var3 = tupla
print(var1)
print(var2)
print(var3)


#conversion de tupla a lista
tupla = (1,2,3)
print(list(tupla))

#tupla a string(cadena)
tupla_c: tuple = ('h','o','l','a')
print(tupla_c)
#convertir a string
print(''.join(tupla_c))

#diccionario
mi_diccionario: dict = {
    '01' : 'Los nuevos gigantes',
    '02' : 'el fantasma de java'
}

print(list(mi_diccionario))
print(mi_diccionario)
print(list(mi_diccionario.values()))
print(list(mi_diccionario.items()))

print(list(mi_diccionario.items())[0])
print(list(mi_diccionario.items())[0][0])

numeros: list = [1,2,3,4,5,6]
caracteres: list = [ str(x) for x in numeros]
print(''.join(caracteres))




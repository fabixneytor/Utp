

lista = [1, 2, 3, 4, "hola mundo", 'a', 11.1, True]
print(lista)
#añadir valores a la lista
lista.append(5)
print(lista)

#cambiar valores d ela lista
lista[2] = 10
print(lista)


lista2 = [8,2,5,1,5,2,1,5,0,10]
#cuantas veces esta el 5 en la lista
#forma larga
contador = 0
for x in lista2:
    if x == 5:
        contador += 1

print("el numero 5 esta ", contador, "veces")
#forma sencilla
print(lista2.count(5))



#añadir una lista a otra lista
lista3 = ["fresa", "papa", "yuca"]
lista2.extend(lista3)
print(lista2)

#limpiar una lista
lista2.clear()
print(lista2)

#en que posicion de la lista esta un elemento
indice = lista3.index("yuca")
print(indice)

#remover un valor o elemento de una lista
elemento = lista3.pop()
print("el elemento elimiado es", elemento)
print(lista3)

#ordenar una lista
frutas = ["fresa", "manzana", "banana", "piña"]
frutas.sort()
print(frutas)


#listas
notas = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15]]
suma = 0
for n in notas:
    for m in n:
        print(m)
        suma += m
    print("La suma de las notas es igual ", suma)
    suma = 0
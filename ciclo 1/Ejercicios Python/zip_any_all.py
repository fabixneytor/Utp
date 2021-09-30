

#zip, crea una lista de tuplas a partir de dos listas
hombres = ["Juan", "Pedro", "Luis"]
mujeres = ["Martha", "Juliana", "Laila"]
#convertimos el objeto a una lista
print (list(zip(hombres, mujeres)))
#convertimos el objeto a una tupla
print (tuple(zip(hombres, mujeres)))
#convertimos el objeto a un conjunto
print (set(zip(hombres, mujeres)))


#any -> al menos un elemento debe ser verdadero
condiciones = [1==2, 2==1, True, False]
if any(condiciones):
    print("al menos un elemento es verdadero")
else:
    print("todos los elementos son falsos")

#all -> todos los elemnetos son verdaderos
if all(condiciones):
    print("todos los elementos son verdaderos")
else:
    print("al menos un elemento es falso")
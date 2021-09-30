

#condicionales con tuplas
tupla1 = (1, 4, 1)
tupla2 = (0, 3, 4)
if tupla1 < tupla2:
    print("cumple")
else:
    print("no cumple")


#variable de tipo entero
var1, var2 = 10, 20

#tupla
var1 = 10, 20 

d = {
    'a' : 10,
    'b' : 1,
    'c' : 22
}

t = list(d.items())
for llave, valor in t:
    print(llave)
    print(valor)


tupla = ([1,2], 5, 10, "hola mundo", True)
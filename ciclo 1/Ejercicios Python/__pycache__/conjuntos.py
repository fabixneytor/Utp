
#diciconario vacio
diccionario = {}

diccionario = {"clave" : 20}


#conjunto vacio
conjunto = set()

conjunto = {1,2,3,5,10}
conjunto.add(6)
print(conjunto)

conjunto2 = set(range(0,11))
print(conjunto2)

a = {1,2,3,4}
b = {2,3}
print(a.intersection(b))
c = a - b
a.difference_update(b)
print(a)
print(c)



for x in range(0, 10):
    print(x)


for j in range(10, 0, -2):
    print("Estamos en la intinerancia " + str(j))



oracion = "Fabian entiende muy bien Python"
frase = oracion.split()
print(frase)

for x in range(0, len(frase)):
    print(frase[x])



personas = {
    "persona1" : "juan",
    "persona2" : "pedro",
    "persona3" : "martha",
    "edad1" : 20
}

for llave in personas:
    print(personas[llave])

for llave, valor in personas.items():
    print("Llave: ", llave, " --- Valor: ", valor)


edad = dict()

for x in range(1, 20):
    llave = "edad" +str(x)
    edad[llave] = x * 2

print("edades-->", edad)
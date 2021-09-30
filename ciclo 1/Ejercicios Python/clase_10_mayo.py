
#estructuras de decision simple
#booleanos

estudiante: bool = True
trabajador: bool = True

if estudiante and trabajador:
    print("cumple la condicion")

else:
    print("no se cumple la condicion")

estudiante: bool = False
trabajador: bool = False

if estudiante or trabajador:
    print("cumple la condicion")

else:
    print("no se cumple la condicion")



if not estudiante and not trabajador:
    print("cumple la condicion")

else:
    print("no se cumple la condicion")


valor1 = 10
valor2 = 8

if valor1 == valor2:
    print("cumple la condicion")

else:
    print("no se cumple la condicion")


if valor1 > valor2:
    if valor1 == 20:
        print("cumple la condicion")
    else:
        print("no cumple if anidado")

elif valor2 > valor1:
    if valor2 ==8:
        print("no se cumple la condicion")



import random

def adivina_numero(numero: int):
    valor_base: int = random.randint(1,2)
    if numero == valor_base:
        print("penitencia")
    else:
        print("no adivino")

numero: int = int(input("adivina el numero"))
adivina_numero(numero)




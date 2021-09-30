from os import system
import random

system("cls")

longitud: int = 5

abedecedario:str = '1234567890abcdefghijklmnñopqrstuvxyz'
# elije aleatoriamente 5 elementos del abecedario
desordenar: list = random.sample(abedecedario, longitud)
#join crea cadenas a partir de objetos iterables
palabra: str = ''.join(desordenar)

print(palabra)
X: str = input("Ingrese el codigo que ves en pantalla: ")
if X == palabra:
    print("El codigo es correcto")
else:
    print('El codigo es incorrecto')

input('presiona enter para salir')
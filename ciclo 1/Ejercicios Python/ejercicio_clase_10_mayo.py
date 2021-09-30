
"""
ejercicio:
codifique un juego de la siguiente manera:
si el usuario adivina la edad del sistema (20 años),
suma 10 puntos, si adivina el nombre del sistema (d3bn1x)
suma 20 puntos sino resta 25 puntos, si adivina la ciudad 
(medellin) suma 35 puntos sino resta 15 puntos.
al final imprima en pantalla el totatl de puntos acumulados
"""

#solucion

def juego_puntos():
    puntos: int = 0

    #solicita la edad del sistema al usuario
    edad: int = int(input("que edad tiene el sistema?"))
    if edad == 20:
        puntos += 10
    nombre: str = input("nombre sistema?")
    if nombre == "d3bn1x":
        puntos += 20
    else:
        puntos -= 25
    ciudad: str = input("ciudad?")
    if ciudad == "medellin":
        puntos += 35
    else:
        puntos -= 15
    return puntos

puntos_acumulados: int = juego_puntos()

print("puntos acumulados= "+ str(puntos_acumulados))
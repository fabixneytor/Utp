
def promedio_tres_dias(dia1, dia2, dia3):
    promedio_dias =  (dia1 + dia2 + dia3) / 3
    return promedio_dias


def promedio_semana(dia1, dia2, dia3, dia4, dia5, dia6, dia7):
    promedio_dias = promedio_tres_dias(dia1, dia2, dia3)
    print("el promedio de los primeros tres dias es:", promedio_dias)
    promedio = (dia1 + dia2 + dia3 + dia4 + dia5 + dia6 + dia7) / 7
    return promedio

resultado = promedio_semana(10, 60, 90, 30, 20, 45, 55)
print("el promedio semanal es", resultado)

'''
RECIBIR VALORES POR CONSOLA
'''
number1 = int(input("por favor ingrese un numero: "))
print("el numero ingresado es: ", number1)
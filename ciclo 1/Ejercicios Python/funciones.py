

'''
ejericicio 1:
    desarrolle una funcion que retorne
    el resultado maximo
    de las siguientes formulas:
    --> ((a/b)-c) * 2 
    --> (5*a-b) /c
    --> mostrar en pantalla cual fue el resultado minimo

'''

#ejercicio 1

def formula1(a, b, c):
    var1= ((a / b) - c) * 2
    var2= (5 * a - b) / c
    maximo = max(var1, var2)
    return maximo

resultado = formula1(5, 10, 20)
print("el valor maximo de la formula es:", resultado)


'''


ejericio 2:
    desarrolle dos funciones,
    cada funcion debe encontrar el promedio de:
    -->funcion1 : promedio de ventas de 3 dias
    -->funcion2 : promedio de ventas de 7 dias
    -->mostrar en consola el resultado de cada funcion y adicionlamnete
    indicar que funcion arrojo el resultado mayor
    y cual arrojo el resultado minimo
'''


#ejercicio 2

#funcion paar calcular el promedio de ventas de 3 dias

def promedio_ventas1(dia1, dia2, dia3):
    promedio = (dia1+dia2+dia3) / 3
    return promedio

#funcion paar calcular el promedio de ventas de 7 dias

def promedio_ventas2(dia1, dia2, dia3, dia4, dia5, dia6, dia7):
    promedio = (dia1+dia2+dia3+dia4+dia5+dia6+dia7) / 7
    return promedio


#mostrar en pantalla los resultados

promedio1 = promedio_ventas1(100000, 50000, 20000)
print("promedio de venta 1", promedio1)

promedio2 = promedio_ventas2(10, 100, 300, 500, 600, 350, 420)
print("promedio de venta 2", promedio2)

print("el resultado mayor es:", max(promedio1, promedio2))
print("el resultado menor es:", min(promedio1, promedio2))

def resultado_concatenado(numero, cadena):
    var = cadena + str(numero)
    return var

print(resultado_concatenado(10, "cadena concatenado"))

#funciones con parametros opcionales

def parametros_opcionales(numero1: int, numero2: int = 0):
    suma = numero1 + numero2
    return suma

resultado = parametros_opcionales(5, 10)

print("resultado:", resultado)

def funcion1(numero1: int, numero2: int = 0):
    suma = numero1 + numero2
    return suma

def funcion2(a: int):
    var = funcion1(a, 10)
    return var

def funcion3():
    var = funcion2(90)
    return var

print(funcion3( ))






#esto es un comentario de una linea en python

'''
esto es una impresion
en consola
del hola Mundo
'''



print('-------------')
print('Hola Mundo')
print('-------------')

#salto de linea \n
'''
Hola
Mundo con salto de linea
\n
'''
print("Hola\nMundo")

#primer ejercicio

print("el conocimiento\nes el principio del todo")
print("---------------------\n--piensa diferente--\n---------------------")

#tabulador \t
print("usuario:\tfabixneytor@hotmail.com")

#ejericio 2

print("mostrar en consola:")
print("user:\tpepito_perez")
print("pass:\t12345")
print("rol:\tadmin")



#ejercicio 3

print("Bienvenido\nHora de ingreso:\t14:00")

#ejercicio 4

print("------------------\n--Bienvenido\t:)\n--A la disrupcion\n--Del conocimiento\n------------------")

#como crear una variable

a = 8
b = a
c = a+b

print(c)

print("primer valor a")
a = 8
print(a)

print("segundo valor a")
a = 10
print(a)

print("tercer valor a")
a = 3.344
print(a)


#ejercicio 5

lado1 = 5
lado2 = 5
lado3 = 5
lado4 = 5

a = b = c = d = 5

perimetro = lado1+lado2+lado3+lado4
perimetro = a+b+c+d
print(perimetro)

#5, 10, 15 suma

lado1, lado2, lado3 = 5.5,10,15

perimetro2 = lado1 + lado2 + lado3

print(perimetro2)

# tipo de datos o variable
f: int = 8
g: float = 10.5

print(type(f))
print(type(g))

#castear una variable

h: int = int(g)
print(h)


#castear variables con sus respectivos valores

number = 10
mensaje1 = "el valor de numer"
mensaje2 = " Es: "+str(number)
mensaje_final = mensaje1 + mensaje2
#muestra en pantalla
print(mensaje_final)

#concatenar palabras y numeros

perimetro = 30
mensaje = str(perimetro)+"cm"
print(mensaje)


#ejercicio 6

'''
mes = 30
semana = 7
semana_por_mes = aqui va el resultado
numero de semanas en el mes: ----

'''
mes = 30
semana = 7
semana_por_mes = int(mes/semana)
print("numero de semanas en el mes: "+str(semana_por_mes))


#ejercicio 7

'''
promedio ventas:
dia1 = 50000
dia2 = 120000
dia3 = 80000
promedio ventas =
'''
dia1 = 50000
dia2 = 120000
dia3 = 80000
promedio_ventas1 = (dia1+dia2+dia3) /3
print("El primer promedio de ventas es: "+str(promedio_ventas1))

#segundo promedio de ventas
promedio_ventas2 = 30000
suma = promedio_ventas2 + int(promedio_ventas1)
print("suma:", suma)
palabra, valor = "suma", suma
print(palabra, valor, "palabra")


#multiplicacion y elevado

multiplicacion = 5 * 2
elevado = 5 ** 2
print(multiplicacion)
print(elevado)




#funcion

def mi_primera_funcion():
    suma1 = (5+10)
    return suma1

print("el suma1 es:"+str(mi_primera_funcion()) )

print("el promedio es:"+str(mi_primera_funcion()) )

print("numero de participantes:"+str(mi_primera_funcion()) )




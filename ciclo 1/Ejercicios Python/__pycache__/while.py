
num = 0
while num <= 5:
    print(num)
    num += 1

print("fin del while")


def factorial(n: int) -> int:
    resultado = 1
    numero_actual = 2
    while numero_actual <= n:
        resultado = resultado * numero_actual
        numero_actual += 1
    return resultado

print(factorial(10))




"""
Ejercicio 1
desarrolle un programa que imprima la suma de los terminos impares comprendidos entre 50 y 200.
debe mostrar la formula
ejemplo:  suma = 51+53+55 ...... 199
"""

#solucion

num = 50
s: str = ""
while num < 200:
    num += 1
    if num%2 !=0:
        s += "+ {}".format(num)

s = s[1:]
print("suma = "+s)



n = 10

while n > 0 :
    print("Dentro del while "+str(n))
    n -= 1
else:
    print("FUERA DEL WHITE, DELTRO DEL ELSE")


"""
break ---> nos saca del ciclo
continue ---> 
"""


nu= 10
while nu >= 0:
    print(nu)
    nu -= 1
    if nu == 5:
        break

print("fuera del white")


nu1= 10
while nu1 >= 0:
    nu1 -= 1
    if nu1 == 5:
        continue
    print(nu1)

print("fuera del white")

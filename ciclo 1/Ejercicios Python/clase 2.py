
#funciones

def mi_primera_funcion():
    suma = 8 + 10
    b = suma + 20
    c = suma + b 
    return c

print(mi_primera_funcion())
print("segundo llamado", mi_primera_funcion())

#funciones sin numeros o variables definidas (variable local)

def suma(numero_a, numero_b, numero_c):
    a= (numero_a + numero_b) * numero_c
    return a


resultado = suma(10, 5, 20)
print("resultado: ", resultado)

#ejericcio 1

'''
desarrolle una funcion que retorne el resultado 
de la siguiente formula:
((a+b-c)*5)/d
'''


def formula(numer_a, numer_b, number_c, numer_d):
    f= ((numer_a + numer_b - number_c) * 5) / numer_d
    return f


resultado = formula(10, 9, 3, 2)
print("resultado ejercicio 1:", resultado)


#funcion para obtener el numero maximo

var2 = max(10, 9, 3, 2)
print("numero maximo", var2)

#funcion para obtener el numero minimo

var3 = min(10, 9, 3, 2)
print("numeor minimo", var3)

a = 5
b = 10
c = 90

var4 = min(a, b, c)
print("numeor minimo", var4)

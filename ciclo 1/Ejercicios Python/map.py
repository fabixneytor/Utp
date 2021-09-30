

def elevar_cuadrado(numero):
    return numero**2

lista: list = [1,2,3,4,5,6,7,8,9]


resultado = list(map(elevar_cuadrado, lista))

print(resultado)


#ejercicio

lista_caracteres = ['á', 'ó', 'í', '@']

def conversion(caracter):
    resp = ""
    if caracter == 'á' or caracter == '@':
        resp = 'a'
    elif caracter == 'ó':
        resp = 'o'
    elif caracter == 'í':
        resp = 'i'
    return resp

result = list( map(conversion, lista_caracteres))

print(result)


#casos de prueba

print("******************CASOS DE PRUEBA*****************")
letra = "á"
palabra: str = "olímpica"
parrafo: str = "El perro ladró, la vaca calló, el gato maulló \
    y el pato, que no daba crédito, corrió todo lo que pudo. \
    Fue así como transcurrió otro apacible día en la granja. \
    Bueno, quizás, debí decir un día raro, y es que el león, \
    que se había escapado de la selva, estaba apunto de hacer su entrada"
print(letra)
print(palabra)
print("--------------------TRANSFORMACION-------------------")
print("")



def conversion(caracter):
    resp = caracter
    if caracter == 'á':
        resp = 'a'
    elif caracter == 'é':
        resp = 'e'
    elif caracter == 'ó':
        resp = 'o'
    elif caracter == 'í':
        resp = 'i'
    elif caracter == 'ú':
        resp = 'u'
    return resp

quitar_minusculas = lambda cadena: "".join (list(map(conversion, list(cadena))))
print(quitar_minusculas(palabra))
print(quitar_minusculas(parrafo))



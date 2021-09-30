


#funciones de orden superior
def suma(val1, val2):
    return (val1+val2)

def resta(val1, val2):
    return (val1-val2)

def multiplicacion(val1, val2):
    return (val1*val2)

def division(val1, val2):
    return (val1/val2)

def operacion(funcion, var1, var2):
    print(funcion(var1, var2))

#llamo la operacion con la funcion
operacion(resta, 10, 2)

#promedio con orden superior
def mejor_promedio():
    #funcion hijo
    def promedio(var1,var2,var3):
        return(var1+var2+var3)/3
    ventas(promedio, 20,50)

def ventas(funcion_promedio, var1, var2=0,var3=0):
    print(funcion_promedio(var1,var2,var3))

mejor_promedio()


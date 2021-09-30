

def promedio_notas (notas: dict):
    nota1 = notas["nota1"]
    nota2 = notas["nota2"]
    nota3 = notas["nota3"]
    nota4 = notas["nota4"]
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    return promedio

dic_notas: dict = {
    "nota1": 3,
    "nota2": 5,
    "nota3": 4.5,
    "nota4": 3.8
}

print (promedio_notas(dic_notas))


notas: dict = {
    "nota1": 3,
    "nota2": 5,
    "nota3": 4.5,
    "nota4": 3.8
}

estudiantes: dict = {
    "estudiante1" : "juan",
    "estudiante2" : "pedro",
    "estudiante3" : "fabian"
    }

aula: dict = {
    "notas" : notas,
    "estudiantes" : estudiantes
}

print(aula)


"""
ejercicio1:
un supermercado ofrece a sus clientes diversos descuantos 
em algunos productos, estps productos son:
limpia vidirios --> 20%
arroz --> 30%
papa --> 10%
suavizante --> 50%
retorne un diccionario
con el descuento respectivo a cada producto
"""
#solucion

def descuentos_productos(productos: dict)->dict:
    #calculamos y guardamos el promedio
    limpia_vidrios_desc = productos["limpia vidrios"] * 0.2
    arroz_descuento = productos["arroz"] * 0.3
    papa_descuento = productos["papa"] * 0.1
    suavizante_descuento = productos["suavizante"] * 0.5
#creamos diccionario de respuesta
    respuesta: dict = {
        "limpia vidrios": limpia_vidrios_desc,
        "arroz": arroz_descuento,
        "papa": papa_descuento,
        "suavizante": suavizante_descuento
    }
#retornamos al diccionario
    return respuesta

productos: dict = {
    "limpia vidrios": 10000,
    "arroz": 8000,
    "papa": 5000,
    "suavizante": 20000
}

print(descuentos_productos(productos))


"""
ejercicio2:

"""
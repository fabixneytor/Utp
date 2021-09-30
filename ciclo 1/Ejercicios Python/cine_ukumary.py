
def desperdicio_gaseosa(amigo_1, amigo_2, amigo_3, cap_boton: float):
    persona = {}
    if (amigo_1["capacidad_actual"]+cap_boton) > amigo_1["capacidad_vaso"]:
        persona["amigo_1"] = amigo_1["nombre"]
    if (amigo_2["capacidad_actual"]+cap_boton) > amigo_2["capacidad_vaso"]:
        persona["amigo_2"] = amigo_2["nombre"]
    if (amigo_3["capacidad_actual"]+cap_boton) > amigo_3["capacidad_vaso"]:
        persona["amigo_3"] = amigo_3["nombre"]

    return persona


amigo_1: dict = {
    "nombre" : "juan",
    "capacidad_vaso" : 100,
    "capacidad_actual" :  50
}

amigo_2: dict = {
    "nombre" : "pedro",
    "capacidad_vaso" : 220,
    "capacidad_actual" :  80
}

amigo_3: dict = {
    "nombre" : "pepito",
    "capacidad_vaso" : 80,
    "capacidad_actual" : 20
}

import random
#funcion para seleccionar un numero de manera aleatoria

def btn_aleatorio() :
    cap_btn = 0
    num: int = random.randint(1,4)
    if num == 1:
        cap_btn = 100
    elif num == 2:
        cap_btn = 20
    elif num == 3:
        cap_btn = 200
    else:
        cap_btn = 80
    return cap_btn

#obtiene la capacidad del boton
btn = btn_aleatorio()
print(btn)

#llama la funcion desperdicio_gaseosa y muestra en pantalla el resultado
print(desperdicio_gaseosa(amigo_1, amigo_2, amigo_3, btn))



btn = 100

print(desperdicio_gaseosa(amigo_1, amigo_2, amigo_3, btn))
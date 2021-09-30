"""
ejercicio2:
desarrolle una funcion que reciba como parametro
un diccionario con la informacion de 4 atletas:
    nombrea_atleta
    distancia_recorrida:{
        distancia1: int,
        distancia2: int
    }
calcule el promedio de distancia recorrida de cada 
atleta. retorne el nombre y la distancia promedio
recorrida por el atleta.
"""
def promedio_recorrido(atletas: dict)->dict:
    prom_atleta1 = (atletas["atleta1"]["distancia_recorrida"]["distancia1"]+atletas["atleta1"]["distancia_recorrida"]["distancia1"])/2
    prom_atleta2 = (atletas["atleta2"]["distancia_recorrida"]["distancia1"]+atletas["atleta2"]["distancia_recorrida"]["distancia1"])/2
    prom_atleta3 = (atletas["atleta3"]["distancia_recorrida"]["distancia1"]+atletas["atleta3"]["distancia_recorrida"]["distancia1"])/2
    prom_atleta4 = (atletas["atleta4"]["distancia_recorrida"]["distancia1"]+atletas["atleta4"]["distancia_recorrida"]["distancia1"])/2
    return {
"atleta1":{
        "nombre": atletas["atleta1"]["nombre_atleta"],
        "promedio": prom_atleta1
    },
    "atleta2":{
        "nombre": atletas["atleta2"]["nombre_atleta"],
        "promedio": prom_atleta2
    },
    "atleta3":{
        "nombre": atletas["atleta3"]["nombre_atleta"],
        "promedio": prom_atleta3
    },
    "atleta4":{
        "nombre": atletas["atleta4"]["nombre_atleta"],
        "promedio": prom_atleta4
    }
}
atleta1 = {
    "nombre_atleta": "Juan",
    "distancia_recorrida":{
        "distancia1": 100,
        "distancia2": 140
    }
}
atleta2 = {
    "nombre_atleta": "Juan",
    "distancia_recorrida":{
        "distancia1": 90,
        "distancia2": 110
    }
}
atleta3 = {
    "nombre_atleta": "Juan",
    "distancia_recorrida":{
        "distancia1": 80,
        "distancia2": 120
    }
}
atleta4 = {
    "nombre_atleta": "Juan",
    "distancia_recorrida":{
        "distancia1": 70,
        "distancia2": 130
    }
}
atletas = {
    "atleta1": atleta1,
    "atleta2": atleta2,
    "atleta3": atleta3,
    "atleta4": atleta4
}

print(promedio_recorrido(atletas))

def desenpaquetar(distancia1: int, distancia2: int):
    print("distancia 1 :" + str(distancia1)+"\nDistancia 2 :" + str(distancia2))

desenpaquetar(**atletas["atleta4"]["distancia_recorrida"])
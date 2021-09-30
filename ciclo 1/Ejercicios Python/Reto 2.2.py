def recomendaciones_musicales(diccionario: dict) -> dict:
    if diccionario["edad"] >= 30:
        if diccionario["hiphop"] == 0:
            if diccionario["gangsta_rap"] == 1:
                recomendacion = "The message"
            else:
                recomendacion = "Latinoamérica"
        elif diccionario["underground"] == 0:
            recomendacion = "Lástima"
        elif diccionario["rap"] == 0:
            recomendacion = "Pecador"
        elif diccionario["gangsta_rap"] == 0:
            recomendacion = "Inspiración divina"
        else:
            recomendacion = "A tribe called quest"
    else:
        if diccionario["hiphop"] == 0:
            recomendacion = "Ojos color de sol"
        elif diccionario["underground"] == 0:
            recomendacion = "Es épico"
        elif diccionario["rap"] == 0:
            recomendacion = "Las esenciales"
        elif diccionario["gangsta_rap"] == 0:
            recomendacion = "Eternamente"
        else:
            recomendacion = "Made me do it"

    valor = 2000
    descuento = 0

    if diccionario["tarjeta_virutal"] == 1:
        if recomendacion == "Made me do it":
            descuento = 0.4
        elif recomendacion == "Pecador":
            descuento = 0.5

    valor = valor - (valor * descuento)

    diccionario_respuesta: dict = {
        "usuario": str (f'{diccionario["nombre"]} {diccionario["apellido"]}'),
        "recomendación": str(recomendacion),
        "valor_pagar": valor
    }

    return diccionario_respuesta


datos_persona1: dict = {
    "nombre": str("Andres"),
    "apellido": str("Quintero"),
    "tarjeta_virutal": bool(1),
    "hiphop": bool(1),
    "underground": bool(1),
    "rap": bool(1),
    "gangsta_rap": bool(1),
    "edad": int(18)
}

datos_persona2: dict = {
    "nombre": str("Alex"),
    "apellido": str("Smith"),
    "tarjeta_virutal": bool(0),
    "hiphop": bool(1),
    "underground": bool(0),
    "rap": bool(1),
    "gangsta_rap": bool(1),
    "edad": int(30)
}

print(recomendaciones_musicales(datos_persona1))
print(recomendaciones_musicales(datos_persona2))

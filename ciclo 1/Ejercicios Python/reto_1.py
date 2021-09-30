

def promedio_contagios(region: str, contagios_lunes: int, contagios_martes: int, contagios_miercoles: int, contagios_jueves: int, contagios_viernes: int, contagios_sabado: int, contagios_domingo: int) -> str:
    promedio = (contagios_lunes + contagios_martes + contagios_miercoles + contagios_jueves + contagios_viernes + contagios_sabado + contagios_domingo) / 7
    return  "El promedio de contagios semanal por covid-19 en {} es de {:.1f} personas." .format(region, promedio)

region:str = input("por favor ingrese la region: ")
print("la region es: ", region)


contagios_lunes: int = int (input("por favor ingrese el numero de contagios del dia contagios_lunes: "))
contagios_martes: int = int (input("por favor ingrese el numero de contagios del dia contagios_martes: "))
contagios_miercoles: int = int (input("por favor ingrese el numero de contagios del dia contagios_miercoles: "))
contagios_jueves: int = int (input("por favor ingrese el numero de contagios del dia contagios_jueves: "))
contagios_viernes: int = int (input("por favor ingrese el numero de contagios del dia contagios_viernes: "))
contagios_sabado: int = int (input("por favor ingrese el numero de contagios del dia contagios_sabado: "))
contagios_domingo: int = int (input("por favor ingrese el numero de contagios del dia contagios_domingo: "))

print (promedio_contagios(region, contagios_lunes, contagios_martes, contagios_miercoles, contagios_jueves, contagios_viernes, contagios_sabado, contagios_domingo))

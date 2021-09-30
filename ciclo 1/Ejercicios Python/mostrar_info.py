

import info_persona

nombre:str = info_persona.nombre_persona()

print("el nombre de la persona es", nombre) 


num1: int = int (input("por favor ingrese el primer numero"))
num2: int = int (input("por favor ingrese el segundo numero"))

resultado = info_persona.suma(num1, num2)
print("resultado", resultado)
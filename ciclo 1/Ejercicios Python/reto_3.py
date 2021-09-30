import os
os.system("cls")


def calcular_ingresos(datos: list) -> dict:
    clientes = len(datos) -1
    total_ingresos = 0
    clientes_fijo = 0
    clientes_celular = 0
    ingresos_fijo = 0
    ingresos_celular = 0
    for x in datos:
        total_ingresos += x['valor_pagar']
        if x['tipo_plan'] == 'fijo' :
            ingresos_fijo += x['valor_pagar']
            clientes_fijo += 1
        if x['tipo_plan'] == 'celular' :
            ingresos_celular += x['valor_pagar']
            clientes_celular += 1
    total_ingresos = ingresos_fijo + ingresos_celular
    if clientes_fijo != 0:
        promedio_fijo = (ingresos_fijo/clientes_fijo)
    else:
        promedio_fijo = 0
    if clientes_celular != 0:
        promedio_celular = (ingresos_celular/clientes_celular)
    else:
        promedio_celular = 0
    
    salida: dict = {
        'total': int(total_ingresos),
        'promedio_fijo': round(promedio_fijo, 1),
        'promedio_celular': round(promedio_celular, 1)
    }
    return salida

datos: list = [
    {
        'tipo_plan': 'fijo',
        'valor_pagar' : 250000
    },
    {
        'tipo_plan': 'celular',
        'valor_pagar' : 350000
    },
    

]

print(calcular_ingresos(datos))
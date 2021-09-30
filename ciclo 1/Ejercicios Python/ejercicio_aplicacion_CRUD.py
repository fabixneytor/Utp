#retardar n segundos
#import time
#time.sleep(10)

#funcion para crear una tarea
def create(tareas: dict, clave: str, valor: dict)->dict:
    tareas[clave] = valor
    return tareas

#funcion para leer las tareas
def read(tareas: dict):
    for clave, tarea in tareas.items():
        print('------------------------')
        print(clave, ": ")
        for llave, valor in tarea.items():
            print(llave, " - ", end=' ')
            print(valor)
        print('------------------------')

#funcion para actualizar una tarea
def update(tareas: dict, clave: str, nuevoValor: dict)->dict:
    claves = tareas.keys()
    if clave in claves:
        tareas[clave] = nuevoValor 
    
    return tareas

#funcion para eliminar una tarea
def delete(tareas: dict, llave: str):
    #obtiene todas las llaves del diccionario
    claves = tareas.keys()
    if llave in claves:
        #elimina e item del diccionario
        #con la llave especificada
        tareas.pop(llave)
    #retorna de nuevo el diccionario
    return tareas

#funcion que me representa el menu
#UI(USER INTERFACE)
def menu():
    #diccionario inicial
    tareas = {
    '01': {
        'descripcion': 'Ir a mercar',
        'estado' : 'pendiente',
        'tiempo' : 60
        }
    }
    
    aut: int = 2
    opc: int = 0
    while (opc != 5):
        #pedir los datos inputs
        print('>>>------Gestor de tareas------<<<')
        print('')
        print('1 --> Crear Tarea')
        print('2 --> Consultar todas las tareas')
        print('3 --> Actualiza una tarea')
        print('4 --> Eliminar una tarea')
        print('5 --> Salir')
        print('')
        #solicitar datos al usuario
        opc: int = int((input('Por favor ingrese una opción>>>  ')))
        #llama las funcionalidades segun las opciones
        if opc == 1:
            descripcion: str = input('Descripcion de la tarea: ')
            estado: str = input('Estado de la tarea: ')
            tiempo: int = int(input('Tiempo de ejecucion de la tarea: '))
            #crea el diccionario con los valores del usuario
            val_diccionario = {
                    'descripcion' : descripcion,
                    'estado' : estado,
                    'tiempo' : tiempo
            }
            tareas  = create(tareas, '0'+str(aut), val_diccionario)
            aut += 1
            print("---------------------------")
            print("\t ¡Tarea creada con éxito!")
            print("---------------------------")
        elif opc == 2:
            read(tareas)
        elif opc == 3:
            clave: str = input("Por favor ingrese el ID de la tarea: ")
            claves = tareas.keys()
            if clave in claves:
                descripcion: str = input('Nueva descripcion de la tarea a actualizar: ')
                estado: str = input('Nuevo estado de la tarea: ')
                tiempo: int = int(input('Nuevo tiempo de ejecucion de la tarea: '))
                val_diccionario = {
                    'descripcion' : descripcion,
                    'estado' : estado,
                    'tiempo' : tiempo
                }
                tareas = update(tareas, clave, val_diccionario)
                print("---------------------------")
                print("\t ¡Tarea actualizada con éxito!")
                print("---------------------------")
            else:
                print("---------------------------")
                print("\tLa tarea ingresada no existe")
                print("---------------------------")
                input("Enter para continuar")
                continue
        elif opc == 4:
            clave: str = input("Por favor ingrese el ID de la tarea a eliminar: ")
            claves = tareas.keys()
            if clave in claves:
                tareas = delete(tareas, clave)
            else:
                print("---------------------------")
                print("La tarea ingresada no existe")
                print("---------------------------")
                input("Enter para continuar")
                continue
        
    return

#llama la funcion principal
menu()
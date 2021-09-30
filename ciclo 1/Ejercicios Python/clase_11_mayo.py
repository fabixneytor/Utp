

#if = si ta ta ta es igual a ta ta ta 


var1 = 5
var2 = 10
if var1%2 == 0:
    print("par")
else:
    print("impar")

var1 = 5
var2 = 10
if var2%2 == 0:
    print("par")
else:
    print("impar")


var1 = 5
var2 = 10
var3:bool = True
var4: bool =  False

if not var3 and not var4:
    print("respuesta equis")
else:
    print("respuesta y")




#cadena de caracteres

caracter = 'a'
fruta: str = "banana"
print(fruta[0])
print(fruta[1])
print(fruta[2])
print(fruta[3])
print(fruta[4])
print(fruta[5])

i: int = 0
print(fruta[i+1])

#para saber la cantidad de caracteres

print (fruta[1:])
print (fruta[:3])


celular: str = "30460786466"
if len(celular) > 10:
    print("por favor verifique su numero de caracteres")


#diccionario = dict

supermercado: dict = {
    "fruta1" : "banana" ,
    "fruta2" : "guanabana" ,
    "fruta3" : "sandia" ,
    "verdura1" : "papa" ,
    "aseo1" : "limpia vidrios"
}

print(supermercado)
print(supermercado["fruta3"])
print(supermercado["aseo1"])


def funcion_supermercado(supermercado: dict) :
    return supermercado["fruta2"]

supermercado1: dict = {
    "fruta1" : "banana" ,
    "fruta2" : "guanabana" ,
    "fruta3" : "sandia" ,
    "verdura1" : "papa" ,
    "aseo1" : "limpia vidrios"
}


print(funcion_supermercado(supermercado))



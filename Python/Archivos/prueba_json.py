import json


archivo = open ("Archivos/datos_empleados_ACME.json", "r")
archivo_2 = open ("Archivos/prueba.json", "w")
json.dump([], archivo_2)
archivo_2.close

archivo_2 = open ("Archivos/prueba.json", "r")
lista_1 = json.load(archivo_2)

lista = json.load(archivo)

archivo.close()
archivo_2.close()
#print (lista)

if lista_1 == "":
    print ("Verdadero")

else:
    print (f"Falso, es igual a {lista_1}")

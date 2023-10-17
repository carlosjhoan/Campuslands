#Programa diseñado para permitirle a una librería almacenar en un archivo la información sobre cada uno de sus libros


import json


#Función del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 3:
                print ("Debe ser un numero de 1 a 3.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")
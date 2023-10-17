#Programa diseñado para permitirle a una librería almacenar en un archivo la información sobre cada uno de sus libros
#1. ID
#2. Título
#3. Autor
#4. Precio

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

#Validación de ID existente
def verif_id (lst_libros, msj):
    while True:
        a = 0
        n = 0
        try:
            id_libro  = input(msj)
            if not id_libro.isdigit():
                print ("\nEl ID deber estar compuesto solo de números.\n\n***VUELVA A INGRESAR EL ID, ESTA VEZ DE MANERA CORRECTA***")
                continue

            for i in lst_libros:
                if list(i.keys())[0] == id_libro:
                    n += 1
                    a = 1

                else:
                    pass
            if a == 1:
                print ("\nEste ID ya está asignado a otro libro.\n\nIntente con un ID diferente.")
                continue
            return id_libro
        
        except Exception as e:
            print ("ERROR!!! Se ha producido un error. Vuelva a intentarlo!!!", e)

#Validación del Título del autor y el nombre del Libros
def valid_nombre(msj):
    while True:
        try:
            nombre = input(msj)
            if not nombre.isalnum():
                print ("\nEl nombre solo puede contener números y letras.")
                #input("Presiona una tecla para continuar... ")
                continue
            return nombre

        except Exception as e:
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.", e)

#Validación de un número entero
def valid_precio(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 0:
                print ("\nEl precio no puede ser negativo!\nIngrese un precio que sea correcto.")
                continue
            return num
        
        except ValueError:
            print ("\nERROR!!! Debe ingresar un número entero.")

#Función permite ingresar ID utilizado para BUSCAR o CONSULTAR el libro
def ingresar_id(msj):
    while True:
        try:
            
            id_buscar = input(msj)
            if not id.isdigit():
                print ("\nEl ID solo puede contener números.")
                #input("Presiona una tecla para continuar... ")
                continue
            
            return id_buscar

        except Exception as e:
            print ("Ha ocurrido un ERROR!!!")
            input ("Presion una tecla para continuar... ")


#Función que me permite verificar si el archivo existe. SI no existe lo crea
def verificar_archivo (ruta):
    try:
        archivo = open(ruta, "r")
        lista_libros = json.load(archivo)
        archivo.close
        return lista_libros

    except:
        
        archivo = open(ruta, "w")
        json.dump([], archivo)
        archivo.close()
        archivo = open(ruta, "r")
        lista_libros = json.load(archivo)
        archivo.close
        return lista_libros
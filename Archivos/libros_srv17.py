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
            if not id_buscar.isdigit():
                print ("\nEl ID solo puede contener números.")
                
                continue
            
            return id_buscar

        except Exception as e:
            print ("Ha ocurrido un ERROR!!!")
            input ("Presion una tecla para continuar... ")

def consultar_libro(id_libro, lst_libros):
    a = 0
    for i in lst_libros:
        if id_libro == list(i.keys())[0]:
            print("\n", "=" * 30)
            print ("\tINFORMACIÓN DEL LIBRO")
            print ("=" * 30)
            print (f"Título: {i[f'{id_libro}']['titulo']}")
            print (f"Autor: {i[f'{id_libro}']['autor']}")
            print (f"Precio: ${i[f'{id_libro}']['precio']:,}")
            print ("-" * 30)
            a = 1
        
    if a == 0:
        print("\n", "*" * 50)
        print ("AVISO: Este libro no se encuentra registrado.")
        print("*" * 50)
        
        


#Función que muestra el nombre y ID de los libros. Utilizar en CONSULTAR Libro
def nomb_libros(lst_libros): 
    n = 0
    lst_vac = []
    nom_id = []
    lst_id = []
    list_cons = []
    for i in lst_libros:
        id_lista = list(i.keys())[0]
        lst_id.append(int(id_lista))
        lst_id = sorted(lst_id)
        #n += 1
        nom_id.append(i[f"{id_lista}"]["titulo"])
        nom_id.append(id_lista)
        lst_vac.append(nom_id)
        nom_id = []
        #print (f"{n} -- {i[0]}")
    for j in lst_id:
        for k in lst_vac:
            if j == k[1]:
                list_cons.append(k[0])
                list_cons.append(j)
    return lst_cons


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
    
#Esta función registra el empleado  
def registrar_libro (dicc_libro, ruta):
        archivo = open(ruta, "r")
        lista_libros = json.load(archivo)
        archivo.close()
        lista_libros.append(dicc_libro)

        archivo = open(ruta, "w")
        json.dump(lista_libros, archivo)
        print ("\n", "-*" * 25)
        print ("| El libro se ha registrado correctamente |")
        print ( "-*" * 25)
        input ("\nPresione cualquier tecla para volver al menú principal... ")



#DESARROLLO DEL PROGRAMA

ruta = "Archivos/libros_srv17.json" #ESTA CORRESPONDE A LA RUTA RELATIVA
#lista_empleados = []
while True:
    print ("\n\t      ", "=" * 20)
    opc = menu("""\t\t    LIBRERÍA
                        MENÚ
               ====================

                1 -- Insertar libro.
                2 -- Consultar libro.
                3 -- SALIR.
                            >>>Elegir una opción [1 - 3]: 
                """)

    if opc == 1:
        
        verificar_archivo(ruta) #Verificación o creación del archivo
        lista_libros = verificar_archivo(ruta)
        #print (lista_empleados)
        dicc_libro = {}
        print ("\n      1. INSERTAR LIBRO")
        print ("=" * 30)
        id_libro = verif_id(lista_libros, "\nID: ")
        titulo = valid_nombre("TÍTULO DEL LIBRO: ")
        autor = valid_nombre("NOMBRE DEL AUTOR: ")
        precio = valid_precio("PRECIO ($): ")
        dicc_libro[id_libro] = {"titulo" : titulo, "autor" : autor, "precio" : precio}
        
        registrar_libro(dicc_libro, ruta)

    elif opc == 2:
        lista_libros = verificar_archivo(ruta)
        print ("\n      2. CONSULTAR LIBRO")
        print ("=" * 30)
        n = 0
        list_nomb_id = nomb_libros(lista_libros)
        print ("\n    ", "-" * 65)
        print ("       IND   |      NOMBRE\t\t\t\t|\tID")
        print ("   ", "=" * 65)
        for i in list_nomb_id:  
            n += 1
            print (f"\t{n}    |   {i[0]}            \t|\t{i[1]}")
            print ("   ", "-" * 65)
        
        id_cons = ingresar_id("Ingrese el id del empleado que desea buscar: ")
        consultar_libro(id_cons, lista_libros)
        input ("\nPresione cualquier tyecla para  volver al menú principal... ")


    
    else: 
        si_no = input("""\n¿Está seguro que desea salir? 
                      s -- Sí, deseo salir!!
                      n -- No, deseo continuar!!!""")
        if si_no == "s" or si_no == "S":
            print ("\nEsperamos haberle sido de utilidad.")
            input ("\nPresione cualquier tecla para SALIR... ")
            break
        else:
            input ("\nPresione cualquier tecla para volver al menú... ")
            pass
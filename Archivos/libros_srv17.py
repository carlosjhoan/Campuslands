#Programa diseñado para permitirle a una librería almacenar en un archivo la información sobre cada uno de sus libros
#1. ID
#2. Título
#3. Autor
#4. Precio

import json


#Función del menú principal
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 6:
                print ("Debe ser un numero de 1 a 6.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")

#Función del menú para editar información del libro
def menu_modif(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 4:
                print ("Debe ser un numero de 1 a 4.")
                
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

#Validación del titulo
def valid_titulo(msj):
    while True:
        try:
            titulo = input(msj)

            return titulo

        except Exception as e:
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.", e)

#Validación del autor
def valid_autor(msj):
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
            print ("    INFORMACIÓN DEL LIBRO")
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
        tit = i[f"{id_lista}"]["titulo"]
        if len(tit) <= 10:
            tit = tit + "              "
        
        elif len(tit) > 10 and len(tit) < 20:
            tit = tit + "        "

        nom_id.append(tit)
        nom_id.append(id_lista)
        lst_vac.append(nom_id)
        nom_id = []
        #print (f"{n} -- {i[0]}")
    for j in lst_id:
        for k in lst_vac:
            if str(j) == k[1]:
                
                nom_id.append(k[0])
                nom_id.append(k[1])
                list_cons.append(nom_id)
                nom_id = []

    return list_cons


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
    
#Esta función registra el libro  
def registrar_libro (dicc_libro, ruta):
        list_id = []
        list_libros_ord = []
        archivo = open(ruta, "r")
        lista_libros = json.load(archivo)
        archivo.close()
        lista_libros.append(dicc_libro)
        for i in lista_libros:
            id_i = list(i.keys())[0]
            list_id.append(int(id_i))
        list_id = sorted(list_id)

        for j in list_id:
            for k in lista_libros:
                if str(j) == list(k.keys())[0]:
                    list_libros_ord.append(k)



        archivo = open(ruta, "w")
        json.dump(list_libros_ord, archivo)
        archivo.close()
        print ("\n", "-*" * 25)
        print ("| El libro se ha registrado correctamente |")
        print ( "-*" * 25)
        input ("\nPresione cualquier tecla para volver al menú principal... ")

#Esta función registra el libro  
def cargar_libro (lsta_libros, ruta):


        archivo = open(ruta, "w")
        json.dump(lsta_libros, archivo)
        archivo.close()
        


#DESARROLLO DEL PROGRAMA

ruta = "Archivos/libros_srv17.json" #ESTA CORRESPONDE A LA RUTA RELATIVA
#lista_empleados = []
while True:
    print ("\n\t      ", "=" * 20)
    opc = menu("""\t\t      LIBRERÍA
                        MENÚ
               ====================

                1 -- Insertar libro.
                2 -- Consultar libro.
                3 -- Editar libro.
                4 -- Borrar libro.
                5 -- Listar libros 
                6 -- SALIR.
                            >>>Elegir una opción [1 - 6]: 
                """)

    if opc == 1:
        
        verificar_archivo(ruta) #Verificación o creación del archivo
        lista_libros = verificar_archivo(ruta)
        #print (lista_empleados)
        dicc_libro = {}
        print ("\n      1. INSERTAR LIBRO")
        print ("=" * 30)
        id_libro = verif_id(lista_libros, "\nID: ")
        titulo = valid_titulo("TÍTULO DEL LIBRO: ")
        autor = valid_autor("NOMBRE DEL AUTOR: ")
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
            print (f"\t{n}    |   {i[0]}     \t\t|\t{i[1]}")
            print ("   ", "-" * 65)
        
        id_cons = ingresar_id("Ingrese el id del libro que desea buscar: ")
        consultar_libro(id_cons, lista_libros)
        input ("\nPresione cualquier tyecla para  volver al menú principal... ")

    elif opc == 3:
        lista_libros = verificar_archivo(ruta)
        print (lista_libros[0]["13"]["precio"])
        print ("\n      3. EDITAR LIBRO")
        print ("=" * 30)
        
        list_nomb_id = nomb_libros(lista_libros)
        print ("\n    ", "-" * 65)
        print ("       IND   |      NOMBRE\t\t\t\t|\tID")
        print ("   ", "=" * 65)
        n = 0
        for i in list_nomb_id:  
            n += 1
            print (f"\t{n}    |   {i[0]}     \t\t|\t{i[1]}")
            print ("   ", "-" * 65)
        
        id_edit = ingresar_id("Ingrese el ID del libro que desea editar: ")

        opc_modif = menu_modif("""Qué desea editarar?
                                1 -- Titulo
                                2 -- Autor
                                3 -- Precio
                                4 -- Dejar todo igual
                               
                               >>> ¿Opción [1 - 4]? """)

        cont = 0
        for j in lista_libros:
            a = 0
            cont += 1
            if list(j.keys())[0] == id_edit:
                cont_id = cont 
                #print(cont)       
            

        if opc_modif == 1:
            lista_libros[cont_id-1][id_edit]["titulo"] =  valid_titulo("NUEVO TÍTULO: ")
            cargar_libro (lista_libros, ruta)
            print ("\n", "-*" * 15)
            print (f"se ha editado el título del libro con ID {id_edit}!!")
            print ( "-*" * 15)
            input ("\nPresione cualquier tecla para volver al menú principal... ")

        elif opc_modif == 2:
            lista_libros[cont_id-1][id_edit]["autor"] =  valid_autor("NUEVA AUTOR: ")
            cargar_libro (lista_libros, ruta)
            print ("\n", "-*" * 25)
            print (f"se ha editado el nombre del autor del libro con ID {id_edit}!!")
            print ( "-*" * 25)
            input ("\nPresione cualquier tecla para volver al menú principal... ")
        
        elif opc_modif == 3:
            lista_libros[cont_id-1][id_edit]["precio"] = valid_precio("NUEVO PRECIO: ")
            cargar_libro (lista_libros, ruta)
            print ("\n", "-*" * 15)
            print (f"se ha editado el precio del libro con ID {id_edit}!!")
            print ( "-*" * 15)
            input ("\nPresione cualquier tecla para volver al menú principal... ")
        
        else:
            print ("\n", "-/" * 20)
            print ("\nLa información de este libro no se editará.")
            print ("-/" * 20)
            input ("\nPresione cualquier tecla para volver al menú principal... ")




    
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
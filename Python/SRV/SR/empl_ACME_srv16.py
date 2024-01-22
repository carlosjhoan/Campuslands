
import json


#Función del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 5:
                print ("Debe ser un numero de 1 a 5.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")

#Validación del menú de modificación de la información del empleado
def menu_modif(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 5:
                print ("Debe ser un numero de 1 a 5.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")

#Validación del nombre
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
def valid_int(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 0:
                print ("\nSolo se permite el ingreso de valores positivos.\n\n***VUELVA A INGRESAR UN VALOR, ESTA VEZ DE MANERA CORRECTA***")
                continue
            return num
        
        except ValueError:
            print ("\nERROR!!! Debe ingresar un número entero.")

#Validación del teléfono
def valid_telefono(msj):
    while True:
        try:
            tel = input(msj)
            if not tel.isdigit():
                print ("\nEl teléfono solo puede contener números.")
                #input("Presiona una tecla para continuar... ")
                continue
            return tel

        except Exception as e:
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.")

#Validación de ID existente
def verif_id (lst_empleados, msj):
    while True:
        a = 0
        n = 0
        try:
            id_empl  = input(msj)
            if not id_empl.isdigit():
                print ("\nEl ID deber estar compuesto solo de números.\n\n***VUELVA A INGRESAR EL ID, ESTA VEZ DE MANERA CORRECTA***")
                continue

            for i in lst_empleados:
                if list(i.keys())[0] == id_empl:
                    n += 1
                    a = 1

                else:
                    pass
            if a == 1:
                print ("\nEste ID ya está asignado a otro empleado.\n\nIntente con un ID diferente.")
                continue
            return id_empl
        
        except Exception as e:
            print ("ERROR!!! Se ha producido un error. Vuelva a intentarlo!!!", e)

#Función permite ingresar ID
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
            input ("Presion una tecla pra continuar... ")


#Función que muestra el nombre de los empleados
def nomb_empleados(lst_empleados): 
    n = 0
    lst_vac = []
    nom_id = []
    for i in lst_empleados:
        id_lista = list(i.keys())[0]
        n += 1
        nom_id.append(i[f"{id_lista}"]["nombre"])
        nom_id.append(id_lista)
        lst_vac.append(nom_id)
        nom_id = []
        #print (f"{n} -- {i[0]}")
    return lst_vac

#Validación del sexo
def valid_sexo(msj):
    while True:
        try:
            sex = input(msj)
            if not (sex == "m" or sex == "M" or sex == "F" or sex == "f"):
                print ("\nSolo se vale ingresar las letras M o F para indicar el sexo.")
                #input("Presiona una tecla para continuar... ")
                continue
            return sex

        except Exception as e:
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.")

#Función que me permite verificar si el archivo existe
def verificar_archivo (ruta):
    try:
        archivo = open(ruta, "r")
        lista_empleados = json.load(archivo)
        archivo.close
        return lista_empleados

    except:
        
        archivo = open(ruta, "w")
        json.dump([], archivo)
        archivo.close()
        archivo = open(ruta, "r")
        lista_empleados = json.load(archivo)
        archivo.close
        return lista_empleados

#Esta función registra el empleado  
def registrar_empleado (dicc_empl, ruta):
        archivo = open(ruta, "r")
        lista_empleados = json.load(archivo)
        archivo.close()
        lista_empleados.append(dicc_empl)

        archivo = open(ruta, "w")
        json.dump(lista_empleados, archivo)
        print ("\n", "-*" * 25)
        print ("| El empleado se ha registrado correctamente |")
        print ( "-*" * 25)
        input ("\nPresione cualquier tecla para volver al menú principal... ")
            
        #return lista_empleados


    

    
#DESARROLLO DEL PROGRAMA

ruta = "Archivos/empl_ACME_srv16.json"
#lista_empleados = []
while True:
    print ("\n\t      ", "=" * 20)
    opc = menu("""\t\t    NÓMINA ACME
                        MENÚ
               ====================

                1 -- Agregar empleado.
                2 -- Modificar empleado.
                3 -- Eliminar empleado.
                4 -- Buscar empleado.
                5 -- SALIR.
                            >>>Elegir una opción [1 - 5]: 
                """)

    if opc == 1:
        
        verificar_archivo(ruta) #Verificación o creación del archivo
        lista_empleados = verificar_archivo(ruta)
        #print (lista_empleados)
        dicc_empleado = {}
        print ("\n      1. AGREGAR EMPLEADO")
        print ("=" * 30)
        id_empl = verif_id(lista_empleados, "\nID: ")
        nombre = valid_nombre("NOMBRE: ")
        edad = valid_int("EDAD: ")
        sexo = valid_sexo("SEXO [M/F]: ")
        telefono = valid_telefono("TELÉFONO: ")
        dicc_empleado[id_empl] = {"nombre" : nombre, "edad" : edad, "sexo" : sexo, "telefono" : telefono}
        
        registrar_empleado (dicc_empleado, ruta)

    elif opc == 2:
        lista_empleados = verificar_archivo(ruta)
        print ("\n      2. MODIFICAR EMPLEADO")
        print ("=" * 30)
        n = 0
        list_nomb_id = nomb_empleados(lista_empleados)
        print ("\n    ", "-" * 50)
        print ("       IND   |      NOMBRE\t\t|\tID")
        print ("   ", "=" * 50)
        for i in list_nomb_id:  
            n += 1
            print (f"\t{n}    |   {i[0]}              \t|\t{i[1]}")
            print ("   ", "-" * 50)
        
        id_modif = ingresar_id("Ingrese el id del empleado que desea buscar: ")

        opc_modif = menu_modif("""Qué desea modificar?
                                1 -- Nombre
                                2 -- Edad
                                3 -- Sexo [M/F]
                                4 -- Teléfono
                                5 -- Dejar todo igual
                               
                               >>> ¿Opción [1 - 5]? """)
        cont = 0
        for j in lista_empleados:
            if list(j.keys())[0] == id_modif:
                cont += 1 
                 
            

        if opc_modif == 1:
            lista_empleados[cont - 1][f"{id_modif}"]["nombre"] =  valid_nombre("NUEVO NOMBRE: ")

        elif opc_modif == 2:
            lista_empleados[cont - 1][f"{id_modif}"]["edad"] =  valid_int("NUEVA EDAD: ")
        
        elif opc_modif == 3:
            lista_empleados[cont - 1][f"{id_modif}"]["sexo"] = valid_sexo("NUEVO SEXO: ")

        elif opc_modif == 4:
            lista_empleados[cont - 1][f"{id_modif}"]["sexo"] = valid_telefono("NUEVO TELÉFONO: ")


        else:
            print ("\nTodo quedará igual.")
            pass
        input ("\nPresione cualquier tecla para volver al menú... ")

        

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
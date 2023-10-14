
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
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.")

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

#Validación del nombre
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
        print ("\n", "-*" * 40)
        print ("El empleado se ha registrado correctamente")
        print ( "-*" * 40)
            
        #return lista_empleados


    

    


ruta = "Archivos/empl_ACME_srv16.json"
#lista_empleados = []
#Aquí se encuentra el desarrollo del programa
while True:
    print ("\n", "=" * 30)
    opc = menu("""NÓMINA ACME
                    MENÚ
               ===================

                1 -- Agregar empleado.
                2 -- Modificar empleado.
                3 -- Eliminar empleado.
                4 -- Buscar empleado.
                5 -- SALIR.
                            >>>Elegir una opción [1 - 8]: 
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
        sexo = valid_sexo("SEXO: ")
        telefono = valid_telefono("TELÉFONO: ")
        dicc_empleado[id_empl] = {"nombre" : nombre, "edad" : edad, "sexo" : sexo, "telefono" : telefono}
        
        registrar_empleado (dicc_empleado, ruta)


    




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
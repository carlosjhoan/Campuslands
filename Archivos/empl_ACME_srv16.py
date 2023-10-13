
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

#Validación de ID existente
def verif_id (lst_empleados, msj):
    while True:
        a = 0
        try:
            id  = input(msj)
            if not id.isdigit():
                print ("\nEl ID deber estar compuesto solo de números.\n\n***VUELVA A INGRESAR EL ID, ESTA VEZ DE MANERA CORRECTA***")
                continue

            for i in list_productos:
                if i["id"] == id:
                    a = 1
                else:
                    pass
            if a == 1:
                print ("\nEste ID ya está asignado a otro producto.\n\nIntente con un ID diferente.")
                continue
            return id
        except Exception as e:
            print ("ERROR!!! Se ha producido un error. Vuelva a intentarlo!!!", e)

#Función que me permite abrir o crear un archivo
def cregistrar_empleado (lst_empleados, ruta):
    try:
        archivo = open(ruta, "r")
        return archivo

    except:
        archivo = open(ruta, "w")
        return archivo
    


ruta = "Archivos/empl_ACME_srv16.py"
lista_empleados = []
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
        lst_empleado = []
        dicc_empleado = {}
        print ("\n      1. AGREGAR EMPLEADO")
        print ("=" * 30)
        id = verif_id("\nID: ")
        nombre = valid_nombre("NOMBRE: ")
        edad = valid_int("EDAD: ")
        sexo = valid_sexo("SEXO: ")
        telefono = valid_telef("TELÉFONO: ")
    




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
import json


def guardar_empleado(lst_personal, ruta):
    try:
        fd = open(ruta, "w")

    except Exception as e:
        print ("Error al abrir el archivo para guardar empleado.", e)
        return None
    
    try:
        json.dump(lst_personal, fd)
    except Exception as e:
        print ("Error al guardar la información del empleado.\n", e)
        return None

    fd.close()
    return True

def existed_ID(id, lst_personal):
    for datos in lst_personal:
        k = list(datos.keys()[0])
        if int(k) == id:
            return True
    return False


def agregar_personal(lst_personal, ruta):
    print ("\n\n1. Agregar Personal")

    id = int(input("\nIngrese el ID: "))
    while existed_ID(id, lst_personal):
        print ("IMPORTANTE: Ya existe alguien con ese ID")
        input()
        id = int(input("\nIngrese el ID: "))
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    telefono = input("Telefono: ")

    dicc_empleado = {}
    dicc_empleado[id] = {"nombre" : nombre, "edad" : edad, "sexo" : sexo, "telefono" : telefono}
    lst_personal.append(dicc_empleado)
    guardar_empleado(lst_personal, ruta)

    if guardar_empleado(lst_personal, ruta) == True:

        input ("El empleado ha sido registrado con éxito\nPresione cualquier tecla para volver al menú... ")
    else:
        print ("ocurrió algún error al guardar el empleado")


def borrar_personal(lst_personal, ruta_file):
    print ("\n\n3. Borrar Personal.")

    id = int(input("\nIngrese el ID: "))
    if not existed_ID(id, lst_personal):
        print ("No existe un empleado con ese ID")
        input ()
        return
    for i in range(len(lst_personal)):
        datos = lst_personal[i]
        k = int(list(datos.keys()[0]))
        if k == id:
            del lst_personal[i]
            print
            break

    if guardar_empleado(lst_personal, ruta_file):
        print ("El empleado ha sido borrado con éxito")
    else:
        print ("Ocurrió un error al eliminar ")

def menu():
    while True:
        try:
            opc = int(input("""REGISTRO PERSONAL
                            1. Añadir
                            2. Editar
                            3. Borrar
                            4. Ver
                            5. Salir

                            >> Opcion [1 - 5]: 
                            """))
            if opc < 1 or opc > 5:
                print ("\nIMPORTANTE: Solo se pueden ingresar opciones entre 1 y 5.\n\nVuelva a intentarlo!!")
                continue
            return opc
        
        except ValueError:
            print ("ERROR!!!\nSolo se permite el ingreso de números enteros... ")

def cargar_info(lst_personal, ruta):
    try:
        fd = open(ruta, "r")

    except Exception as e:
        try:
            fd = open(ruta, "w")

        except Exception as d:
            print ("\nError al intentar abrir archivo" + d)
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lst_personal = json.load(fd)

        else:
            lst_personal = []

    except:
        print ("ERROR!!")
        return None
    print (lst_personal)
    fd.close()
    
    return fd


rut_file = "Archivos/datos_empleados_ACME.json"
#"PROGRAMAR PRINCIPAL"
lista_personal = []
lista_personal =cargar_info(lista_personal, rut_file)
while True:
    opc = menu()

    if opc == 1:
        #agregar personal
        agregar_personal(lista_personal, rut_file)

    elif opc == 2:
        pass

    elif opc == 3:
        #pass
        borrar_personal(lista_personal, rut_file)

    elif opc == 2:
        pass

    else:
        pass
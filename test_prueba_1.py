#validación del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 6:
                print ("\nIMPORTANTE: Solo se pueden ingresar opciones entre 1 y 6.\n\nVuelva a intentarlo!!")
                continue
            return opc
        
        except ValueError:
            print ("ERROR!!!\nSolo se permite el ingreso de números enteros... ")


#validación del menú de modificación de un producto
def menu_modif(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 4:
                print ("\nIMPORTANTE: Solo se pueden ingresar opciones entre 1 y 4.\n\nVuelva a intentarlo!!")
                continue
            return opc
        
        except ValueError:
            print ("ERROR!!!\nSolo se permite el ingreso de números enteros... ")

#ingresar ID
def ingresar_id(msj):
    while True:
        try:
            id = input(msj)
            if not id.isdigit():
                print ("\nEl ID deber estar compuest solo de números.\n\n***VUELVA A INGRESAR EL ID, ESTA VEZ DE MANERA CORRECTA***")
                continue
            return id

        except Exception as e:
            print ("\nSe ha producido un error. Vuelva a intentarlo.") 

#Función que verifica si un id se encuentra en la base de datos
def buscar_id(lst, msj):
    while True:
        a = 0
        try:
            id  = input(msj)
            if not id.isdigit():
                print ("\nEl ID deber estar compuesto solo de números.\n\n***VUELVA A INGRESAR EL ID, ESTA VEZ DE MANERA CORRECTA***")
                continue

            for i in lst:
                if i["id"] == id:
                    a = 1
                else:
                    pass

            if a == 1:
                
                return id
            
            else: 
                
                return 0
                
        except Exception as e:
            print ("ERROR!!! Se ha producido un error. Vuelva a intentarlo!!!", e) 

#Validación de ID existente
def verif_id (list_productos, msj):
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

#validación nombre del producto
def valid_nombre(msj):
    while True:
        try:
            nombre = input(msj)
            if not nombre.isalnum():
                print ("\nEl nombre del producto solo puede contener letras y números.\n\n***INGRESE UN NOMBRE VÁLIDO SEGÚN LAS INDICACIONES ANTERIORES***")
                continue

            return nombre
        
        except Exception as e:
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.")

#Lista de nombres y ID
def nombre_id(lst):
    lst_nomb_id = []
    nom_id = []
    for i in lst:
        nom_id.append(i["nombre"])
        nom_id.append(i["id"])
        lst_nomb_id.append(nom_id)
        nom_id =[]
    return lst_nomb_id

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

#Función que obtiene una lista ordenada con todos los precios de los productos de menor a mayor
def list_precios(lst_prod):
    lst_prec = []
    for i in lst_prod:
        lst_prec.append(i["precio"])
    lst_prec = sorted(lst_prec)

    return lst_prec

list_productos = []
producto = {}
while True:
    opc = menu("""   MENÚ
               =======================
                    PRODUCTOS ACME
               =======================
               1. Agregar producto
               2. Modificar producto
               3. Eliminar producto
               4. Listar varios productos
               5. Estrategia de mercadeo
               6. SALIR
               
               >>> ¿Opción [1 - 6]? """)
    if opc == 1:
        print ("\n\n***AGREGAR PRODUCTO***")
        print ("=" * 30)
        id = verif_id (list_productos, "\nID del producto: ")
        producto["id"] = id
        nombre = valid_nombre("\nNombre del producto: ")
        producto["nombre"] = nombre
        precio = valid_int("\nPrecio del producto: ")
        producto["precio"] = precio
        cant_inventario = valid_int("\nUnidades disponibles: ")
        producto["unidades"] = cant_inventario
        list_productos.append(producto)
        producto = {}
        input("\nPresione cualquier tecla para volver al menú principal... ")

    elif opc == 2:
        print ("\n\n***MODIFICAR PRODUCTO***")
        print ("=" * 30)

        print ("\nindicador\t|\tNombre\t|\tid")
        print ("-" * 50)
        lst_nom_id = nombre_id(list_productos)
        n = 1
        for i in lst_nom_id:
            print (f"{n}\t\t|\t{i[0]}\t|\t{i[1]}")
            print ("-" * 50)
            n += 1
        eleg_prod = valid_int("\nIngrese el indicador del producto que desea modificar")
        opc_modif = menu_modif("""   MENÚ DE MODIFICACIÓN
                               ============================
                               1. Modificar el nombre del producto
                               2. Cambiar el precio del producto.
                               3. Modificar las unidades disponibles.
                               4. Dejar todo igual.
                               
                               >>> ¿Opción [1 - 4]? """)
        if opc_modif == 1:
            nombre_antiguo = list_productos[eleg_prod  - 1]["nombre"] 
            list_productos[eleg_prod  - 1]["nombre"] = valid_nombre("\nIngrese el nuevo nombre del producto. ")
            nombre_nuevo = list_productos[eleg_prod  - 1]["nombre"] 
            print ("-" * 50)
            print (f"""Se ha reemplazado el nombre
                   Nombre antiguo: {nombre_antiguo}
                   Nombre nuevo: {nombre_nuevo}""")
            print ("-" * 50)
            input ("\nPresione cualquier tecla para volver al menú principal... ")

        elif opc_modif == 2:
            precio_antiguo = list_productos[eleg_prod  - 1]["precio"]
            list_productos[eleg_prod  - 1]["precio"] = valid_int("\nIngrese el nuevo precio del producto. ")
            precio_nuevo = list_productos[eleg_prod  - 1]["precio"]
            print ("-" * 30)
            print (f""""Se ha reemplazado el precio
                   Precio antiguo: {precio_antiguo}
                   Precio nuevo: {precio_nuevo}""")
            print ("-" * 30)
            input ("\nPresione cualquier tecla para volver al menú principal... ")

        elif opc_modif == 3:
            unidades_antiguo = list_productos[eleg_prod  - 1]["unidades"]
            list_productos[eleg_prod  - 1]["unidades"] = valid_int("\nIngrese la nueva cantidad de unidades disponibles. ")
            unidades_nuevo = list_productos[eleg_prod  - 1]["unidades"]
            print ("-" * 30)
            print (f""""Se ha reemplazado el precio
                   Unidades antiguas: {unidades_antiguo}
                   Unidades nuevas: {unidades_nuevo}""")
            print ("-" * 30)
            input ("\nPresione cualquier tecla para volver al menú principal... ")

        elif opc_modif == 4:
            print ("\n", "=" * 20)
            print ("TODO QUEDARÁ IGUAL!!")
            print ( "=" * 20)
            input ("\nPresione cualquier tecla para volver al menú principal... ")

    elif opc == 3:
        print ("\n\n***ELIMINAR PRODUCTO***")
        print ("=" * 30)
        id_buscar = buscar_id(list_productos, "Ingrese el ID del producto que desea eliminar: ")
        if id_buscar != 0:
            for i in list_productos:
                if i["id"] == id_buscar:
                    list_productos.remove(i)
                    print (f"\nEl producto con ID {id_buscar} se ha eiminado correctamente.")
                    input ("\nPresione culquier tecla para volver al menú principal... ")

                else:
                    pass
        else: 
            print ("\nEste producto no se encuentra en la base de datos. NO SE PUEDE ELIMINAR!!!")
            input ("\nPresione culquier tecla para volver al menú principal... ")

    elif opc == 4:
        pass

    elif opc == 5:
        print ("\n\n***ESTRATEGIA DE MERCADEO***")
        print ("=" * 30)
        lst_prec_ord = list_precios(list_productos)
        n = 0
        permiso = "s"
        seguir = "s"
        while permiso == "s":
            for i in lst_prec_ord:
                for a in list_productos:
                   #while seguir == "s" or seguir == "S":
                        if (seguir == "s" or seguir == "S") and a["precio"] == i:
                            print ("*" * 50)
                            print (f"Nombre del producto: {a['nombre']}")
                            print (f"ID del producto: {a['id']}")
                            print (f"Precio del producto: ${a['precio']:,}")
                            print (f"Unidades disponibles del producto: {a['unidades']}")
                            n += 1
                        else:
                            pass

                        if n == 5:
                            seguir = input ("""\n¿Desea seguir listando los productos? 
                                s -- Sí, deseo seguir listando.
                                n -- No, deseo dejar de listarlos.""")
                            
                            n = 0

                            if seguir == "s" or seguir == "S":
                                pass

                            else:
                                seguir = "n"
             
                                permiso = "f"
            permiso = "n"
                                
        input ("\nPresione cualquier tecla para volver al menú")



    
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

            
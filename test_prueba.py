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

#Validación de ID existente
def verif_id (list_productos, msj):
    while True:
        try:
            id = id = input(msj)
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
            print ("ERROR!!! Se ha producido un error. Vuelva a intentarlo!!!")

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
        id = verif_id (list_productos, "\nID del producto: ")
        producto["id"] = id
        nombre = valid_nombre("\nNombre del producto: ")
        producto["nombre"] = nombre
        precio = valid_int("\nPrecio del producto: ")
        producto["precio"] = precio
        cant_inventario = valid_int("\nUnidades disponibles: ")
        list_productos.append(producto)
        producto = {}
        input("\nPresione cualquier tecla para volver al menú principal... ")

    
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

            
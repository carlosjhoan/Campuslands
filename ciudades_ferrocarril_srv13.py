#Este programa guarda los nombres de las ciudades de los ferrocarriles


#validación del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 3:
                print ("\nIMPORTANTE: Solo se pueden ingresar opciones entre 1 y 3.\n\nElija una opción válida!!")
                continue
            return opc
        
        except ValueError:
            print ("ERROR!!!\nSolo se permite el ingreso de números enteros... ")


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
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.", e)


#Función para crear matrices
def crear_matrices_ceros (fil, col):
    m = []
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m

#Función para llenar matrices
def llenar_matriz (mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat [f][c] = "------------"
        print (" ")

#Validación de la cantidad de ciudades > 0
def valid_int(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 0:
                print ("\nLa cantidad de ciudades debe ser un valor positivo.\n\n***VUELVA A INGRESAR UN VALOR, ESTA VEZ DE MANERA CORRECTA***")
                continue
            return num
        
        except ValueError:
            print ("\nERROR!!! Debe ingresar un número entero.")

mat_ciudades = []

while True:

    print ("\t\t********************")
    opc = menu("""   \t\tRED DE FERROCARRILES
                ********************
               1. Llenar ciudades. 
               2. Verificar ruta directa entre 2 ciudades
               3. SALIR
               
               >>> ¿Opción [1 - 2]? """)

    if opc == 1:
        ciudad_list = []
        ciudad_dicc = {}
        enlaces = {}
        print ("\n", "-" * 60)
        print ("1. Llenar ciudades")
        print ("-" * 60)
        num_ciudades = valid_int("\nCantidade de ciudades: ")
        
        for i in range(num_ciudades):
            ciudad_list = []
            ciudad_dicc = {}
            enlaces_list = []
            enlaces = {}
            nombre_ciudad = valid_nombre(f"\nNombre de la ciudad {i + 1}: ")
            ciudad_dicc["nombre"] = nombre_ciudad
            ciudad_list.append(ciudad_dicc)

            num_enlaces = valid_int(f"\n¿Con cuántas ciudades está enlazada {ciudad_dicc['nombre']}? ")
            for a in range(num_enlaces):
                nombre_enlace = valid_nombre(f"\nEnlace N° {a + 1}: ")
                enlaces_list.append(nombre_enlace)
            enlaces["enlaces"] = enlaces_list
            ciudad_list.append(enlaces)
            mat_ciudades.append(ciudad_list)
        print (mat_ciudades)
        


    elif opc == 2:
        pass

   

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
            

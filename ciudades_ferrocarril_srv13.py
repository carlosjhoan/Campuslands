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
                print ("\nLa cantidade ciudades debe ser un valor positivo.\n\n***VUELVA A INGRESAR UN VALOR, ESTA VEZ DE MANERA CORRECTA***")
                continue
            return num
        
        except ValueError:
            print ("\nERROR!!! Debe ingresar un número entero.")

while True:

    opc = menu(msj)

    if opc == 1:
        pass

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
            pass

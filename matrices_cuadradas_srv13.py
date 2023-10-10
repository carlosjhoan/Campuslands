#Este programa crea e imprime matrices cuadradas que siguen cierto patrón

#Validación del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 9:
                print ("Debe ser entre 1 y 9.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")


#Función que valida la entrada de un número entero que indica el tamaño de la matriz
def valid_int(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 0:
                print ("\nAdivina con números positivos")
                continue
            return num
        
        except ValueError:
            print ("\nERROR!!! Debe ingresar un número entero.")

#Función que crea matrices de ceros
def crear_matrices_ceros (fil, col):
    m = []
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m


#Función que llena matrices consecutivos por fila. Indicador 1
def llenar_matriz_1 (mat):
    n = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            n += 1 
            mat [f][c] = n 
    return mat

#Función que llena matrices consecutivos por columna. Indicador 2
def llenar_matriz_2 (mat):
    n = 0
    for c in range(len(mat)):
        for f in range(len(mat[c])):
            n += 1 
            mat [f][c] = n 
    return mat

def llenar_matriz_3 (mat):
    n_f = 0
    
    fila_impar = list(range(1, len(mat) + 1))
    fila_par = list(reversed(fila_impar))
    #print ("fila_par", fila_par)
    #print ("fila_impar", fila_impar)

    for f in range(len(mat)):
        n_f += 1
        n_c = 0
        for c in range(len(mat[f])):
            #n_c += 1
            if n_f % 2 == 0:
                mat [f][c] = fila_par[c]
            else:
                mat [f][c] = fila_impar[c]

    return mat

def llenar_matriz_45 (mat):
    
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if c == f: 
                mat [f][c] = 1 
    return mat, list(reversed(mat))

        #print (" ")
#Función que imrpime matrices
def print_matrices (mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print (mat[f][c], end = "\t")
        print (" ")

while True:
    print ("\t\t", "=" * 20)
    opc = menu("""\t\t  MATRICES CUADRADAS
                 ====================
               1. Números consecutivos en dirección de las filas
               2. Números consecutivos por columna
               3. Números consecutivos por fila y se devuelve
               4. Matriz diagonal.
               5. Matriz diagonal recíproca.
               6. Mitad inferior de la matriz con 1, la otra con 0.
               7. Mitad superior de la matriz con 1, la otra con 0.
               8. Llenar con A y con B de manera alternada, media matriz.
               9. SALIR
               
               >>> ¿Opción [1 - 9]? """)


    if opc == 1:
        print ("\n", "-" * 60)
        print ("1. Números consecutivos en dirección de las filas")
        print ("-" * 60)
        num_filas = valid_int("\nNúmero de filas de la matriz: ")
        matriz_1 = crear_matrices_ceros (num_filas, num_filas)
        matriz_1_llena = llenar_matriz_1 (matriz_1)
        print_matrices (matriz_1_llena)
        input ("\nPresione una tecla para volver al menú... ")

    elif opc == 2:
        print ("\n", "-" * 60)
        print ("2. Números consecutivos en dirección de las columnas")
        print ("-" * 60)
        num_filas = valid_int("\nNúmero de filas de la matriz: ")
        matriz_2 = crear_matrices_ceros (num_filas, num_filas)
        matriz_2_llena = llenar_matriz_2 (matriz_2)
        print_matrices (matriz_2_llena)
        input ("\nPresione una tecla para volver al menú... ")

    elif opc == 3:
        print ("\n", "-" * 60)
        print ("3. Números consecutivos por fila y se devuelve")
        print ("-" * 60)
        num_filas = valid_int("\nNúmero de filas de la matriz: ")
        matriz_3 = crear_matrices_ceros (num_filas, num_filas)
        matriz_3_llena = llenar_matriz_3 (matriz_3)
        print_matrices (matriz_3_llena)
        input ("\nPresione una tecla para volver al menú... ")

    elif opc == 4:
        print ("\n", "-" * 60)
        print ("4. Matriz diagonal.")
        print ("-" * 60)
        num_filas = valid_int("\nNúmero de filas de la matriz: ")
        matriz_4 = crear_matrices_ceros (num_filas, num_filas)
        matriz_4_llena = llenar_matriz_45 (matriz_4)[0]
        print_matrices (matriz_4_llena)
        input ("\nPresione una tecla para volver al menú... ")

    elif opc == 5:
        print ("\n", "-" * 60)
        print ("5. Matriz diagonal recíproca.")
        print ("-" * 60)
        num_filas = valid_int("\nNúmero de filas de la matriz: ")
        matriz_5 = crear_matrices_ceros (num_filas, num_filas)
        matriz_5_llena = llenar_matriz_45 (matriz_5)[1]
        print_matrices (matriz_5_llena)
        input ("\nPresione una tecla para volver al menú... ")

    elif opc == 6:
        pass

    elif opc == 7:
        pass

    elif opc == 8:
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
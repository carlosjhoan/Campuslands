#Validación del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 3:
                print ("Debe ser un numero de 1 a 3.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")

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

#Validación de un número entero
def n_menor_m(n, msj):
    while True:
        try:
            m = int(input(msj))
            if m < 0:
                print ("\nSolo se permite el ingreso de valores positivos.\n\n***VUELVA A INGRESAR UN VALOR, ESTA VEZ DE MANERA CORRECTA***")
                continue

            elif n > m:
                print ("\nel valor de m no puede ser menor que el de n. Ingrese un valor correcto para m.")
                continue

            return m
        
        except ValueError:
            print ("\nERROR!!! Debe ingresar un número entero.")

#Función que calcula los valores secuenciales recíprocos. Devuelve una lista con los recíprocos y su respectivos signo
def sec_rec(N):
    list_recip = [1]
    sec = "1"
    for i in range(2, N + 1):
        if i % 2 == 0:
            num = -1/i
            sec += f" - 1/{i}"
            list_recip.append(num)
        else:
            num = 1/i
            sec += f" + 1/{i}"
            list_recip.append(num)
    
    
    return list_recip, sec

#Función que devuelve la secuencia de términos como una secuencia string. Esta con el fin de visualizar la secuencia
def sec_str (lst):
    sec = ""
    for i in lst:
        sec += f"{i}"
        
    return sec

#Función que devuelve una lista de primos entre n y m
def primos_n_m (n, m):
    list_primos = []
    divisores_num = []
    sec_primos = ""
    if n == 0:
        n = 1
    for i in range (n, m + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                divisores_num.append(j)
        
        if len(divisores_num) == 2:
            list_primos.append(i)
            sec_primos += f"{i} | "
        divisores_num = []
    return list_primos, sec_primos




while True:
    opc = menu("""\n\t\t   MENÚ 
               ------------
               1. Serie de los recíprocos.
               2. Números primos [n - m].
               3. SALIR
               
               >>> ¿Opción [1 - 3]? """)
    
    if opc == 1:
        print ("\n   SERIE DE LOS RECÍPROCOS")
        print ("=" * 30)
        num_N = valid_int("\nIngrese un entero N: ")
        
        if num_N == 0:
            suma_terminos = 0
            sec_terminos = ""
        else:
            suma_terminos = sum(sec_rec(num_N)[0])
            sec_terminos = sec_rec(num_N)[1]

        print ("\n", "=*" * 50)
        print (f"Secuencia de términos: {sec_terminos}")
        print (f"SUma de los términos: {suma_terminos:.4f}")
        print ("=*" * 50)
        input ("\nPresione cualquier tecla para volver al menú... ")
    
    elif opc == 2:
        print ("\n   NÚMEROS PRIMOS [n - m]")
        print ("=" * 30)
        num_N = valid_int("\nIngrese el valor inicial del rango N: ")
        num_M = n_menor_m(num_N, "\nIngrese el valor final del rango M (M > N): ")
        lista_primos = primos_n_m (num_N, num_M)[0]
        sec_primos = primos_n_m (num_N, num_M)[0]
        print ("\n", "=*" * 35)
        print (f"Valor incicial: {num_N}")
        print (f"Valor incicial: {num_M}")
        print (f"\nPrimos dentro del rango: {sec_primos}")
        print (f"Cantida de primos en el rango: {len(lista_primos)}")
        print ("=*" * 35)
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
        
#Validación del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 4:
                print ("Debe ser un numero de 1 a 4.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")


#Validación del ingreso de un número entero
def int_posit(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 0:
                print ("Deben ser numeros positivos")
                
                continue
            return num
        
        except ValueError:
            print ("ERROR!!! Debe ingresar solo números")
 
#Función factorial
def factorial (n):
    fact = 1
    for i in range (1, n + 1):
        fact *= i
    return fact

#Definición de la función combinatoria
def combinatoria (n, k):
    if k <= n:
        comb = factorial(n) / (factorial(k)  * factorial(n - k) )
        
    else: 
        comb = """No se puede realizar el cálculo.
                k debe ser menor que n."""
    return comb

#Definción de la función que elimina texto
def elimin_texto(secuencia):
    sec_final = ""
    secuencia = secuencia.strip()
    for i in secuencia:
        if i.isdigit() == True:
            sec_final += i
            
            
    if sec_final == "":
        sec_final = "SECUENCIA VACÍA"
            
    return sec_final

#Definición de función que aplica el IVA
def iva (valor_factura, porc_iva):
    valor = (1+(porc_iva/100)) * valor_factura
    return valor

#Ejecución del programa
while True:
    
    opc = menu("""*** MENÚ ***
                  1 -- Cálculo de combinatoria
                  2 -- Convertir texto a número
                  3 -- Calcular el IVA de una factura
                  4 -- SALIR
                  >> Escoja una opción (1 - 4)? """)
    if opc == 1:
        print ("\nCÁLCULO DE LA COMBINATORIA")
        n = int_posit ("Ingrese el valor de n (cantidad de opciones): ")
        k = int_posit ("Ingrese el valor de k (Cantidad de elecciones) [k < n]: ")
        res = combinatoria(n, k)
        print ("\n", "*=" * 20)
        print (f"Cantidad de combinaciones posibles: {int(res)}")
        print ( "*=" * 20)
        input ("\npresione cualquier tecla para volver al menú... ")
        
    elif opc == 2:
        print ("\nELIMINAR TEXTO")
        texto = input ("Ingrese una secuencia de caracteres: ")
        print (f"La secuencia final con solo números es: {elimin_texto(texto)}")
        input ("\npresione cualquier tecla para volver al menú... ")
        
    elif opc == 3:
        print ("\nCALCULAR EL VALOR DE UNA FACTURA APLICANDO IVA")
        factura = int_posit ("Ingrese el valor de la factura SIN IVA: ")
        porc_iva = int_posit ("Ingrese el porcentaje de IVA a aplicar: ")
        fact_iva = iva (factura, porc_iva)
        print (f"\nEl valor dela factura con el IVA aplicado es de: {fact_iva:,.0f}")
        input ("\npresione cualquier tecla para volver al menú... ")
        
    else:
        print ("\nEsperamos haber sido de utilidad.")
        input ("\nPresione cualquier tecla para salir... ")
        break
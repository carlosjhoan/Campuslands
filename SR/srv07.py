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
            print ("ERROR !!! Debe ingresar números entero.")
            

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


#Validación del ingreso de un texto
def valid_texto(msj):
    while True:
        try:
            text = input(msj)
            text = text.strip()
            if not text.isalnum or len(text) == 0:
                print ("Ingrese un texto valido. No puede ser vacio. Debe ser compuesto de solo letras o números.")
                continue
            return text
        
        except Exception as e:
            print ("Texto no válido: ", e)
            
#definición de la función factorial
def factorial (num):
    mult = 1
    for i in range(1, num + 1):
        mult *= i

    return mult
#Definición de la función salario de un trabajador
def salario_trabajador(horas, valor_hora):
    if horas <= 40:
        salario = horas * valor_hora
    

    elif horas > 40:
        salario = (40 * valor_hora) + ((horas-40) * 1.5 * valor_hora)

    
    return salario

#Definción de la función que cuenta palabras de un texto
def cont_palabras(texto):
    texto = texto.strip()
    list = texto.split(" ")
    words = 0
    for i in list:
        
        if i != "":
            words += 1

    return words



#Ejecución del programna
while True:

    opc = menu("""MENÚ
               Presione.
               1 -- Factorial de número
               2 -- Calcular salario de un empleado
               3 Calcular palbras en un párrafo
               4 -- Salir""")
    
    if opc == 1:
        print ("\nCALCULAR EL FACTORIAL DE UN NUMERO")
        num = int_posit("\nIngrese un numero: ")
        

        print ("\n", "-" * 10)
        print (F"Factorial({num}) = {factorial(num)}")
        print ("\n", "-" * 10)
        input("\nPresione cualquier tecla para volver al menú...")

    elif opc == 2:
        print ("\nCALCULAR EL SALARIO DE UN TRABAJADOR")
        horas = int_posit("\nIngrese la cantidad de horas trabajadas por el trabajador: ")
        valor_hora = int_posit("\nIngrese el valor de la hora: ")

        print (f"El salario del trabajador es: {salario_trabajador(horas, valor_hora):,.0f}")
        input ("\nPresione cualquier tecla para volver al menú...")

    elif opc == 3:
        print ("\nCALCULAR EL NÚMERO DE PALABRAS DE UN TEXTO")

        texto = valid_texto("Digite un texto: ")
        print (f"\nEl texto tiene {cont_palabras(texto)} palabras.\n")

    else:
        input("\nPresione cualquier tecla para SALIR...")
        break












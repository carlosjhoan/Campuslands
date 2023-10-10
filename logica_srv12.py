#Juego de Lógica de adivinar número 
#Este código es un juego que permite adivinar un número
import random

#Validación del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 2:
                print ("Debe ser 1 o 2.")
                
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
                print ("\nAdivina con números positivos")
                continue
            return num
        
        except ValueError:
            print ("\nERROR!!! Debe ingresar un número entero.")

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
            print ("Ha ocurrido un ERROR!!!")
            input ("Presion una tecla para continuar... ")

#Función que lista los 10 primeros en la tabla
def list_ganadores(lst):
    lst_int = []
    lst_ord_jugadores = []
    for i in lst:
        lst_int.append(i[1])
    lst_ord = sorted(lst_int)
    for j in lst_ord:
        for k in lst:
            if k[1] == j:
                lst_ord_jugadores.append(k)

    return lst_ord_jugadores

lista_jugadores = []

while True:
    
    print ("\t\t*****************")
    opc = menu("""   \t\tADIVINA EL NÚMERO
                *****************
               1. Nuevo Jugador
               2. SALIR
               
               >>> ¿Opción [1 - 2]? """)
    
    if opc == 1:
        jugar = "s"
        perm_jugar = "s"
        data_jugador = []
        intentos_max = 10
        n = 0
        intentos = 0
        num_adivinar = random.randint(1, 100)
        nombre = valid_nombre("\nNombre del jugador: ")
        data_jugador.append(nombre)
        #num_jugador = valid_int("\n¿Cuál cree que es el número secreto? ")
        #for i in range(1, intentos_max + 1):
        while perm_jugar == "s" or perm_jugar == "S":

            if (jugar == "s" or jugar == "S") and intentos < intentos_max:
                
                intentos += 1
                num_jugador = valid_int(f"\nIntento {intentos}/10\n¿Cuál cree que es el número secreto? ")
                
                if num_jugador == num_adivinar:
                    data_jugador.append(intentos)
                    lista_jugadores.append(data_jugador)
                    lista_ord = list_ganadores(lista_jugadores)
                    data_jugador = []
                    print("\n", "=" * 40)
                    print ("::: LO LOGRASTE!!! :::")
                    print("=" * 40)
                    print ("\n", "-" * 35)
                    print ("\tTABLA DE POSICIONES")
                    print ( "-" * 35)
                    print ("  Jugador\t|\tN° Intentos")
                    print ("=" * 35)
                    #jugar = "n"

                    for a in lista_ord:
                        #if a[0] == nombre:
                            #print ("\n", "*=" * 35)
                            #print (f" {a[0].upper()}\t|\t{a[1]}")
                            #print ( "*=" * 35)

                        #else:
                        print(f" {a[0]}\t|\t{a[1]}")
                        print ("=" * 35)

                    seguir_jugando = input("""\n¿Desea seguir jugando?
                                            s -- Sí, quiero intentarlo de nuevo
                                            n -- No, ya me aburrí
                                            
                                            >>> ¿Qué desea? """)
                    
                    if seguir_jugando == "s" or seguir_jugando == "S":
                        data_jugador.append(nombre)
                        intentos = 0
              
                    else:
                        jugar = "n"
                        perm_jugar = "n"
                        print ("\nQué bueno que lo hayas intentado. Esperamos que te hayas divertido")
                        input("\nPresione cualquier tecla para volver al menú... ")


                else:
                    if num_jugador < num_adivinar:
                        print ("\nFALLASTE!!!\nEl número a adivinar es MAYOR")
                    else:
                        print ("\nFALLASTE!!!\nEl número a adivinar es MENOR")
            else:
                #data_jugador.append(nombre)
                data_jugador.append(intentos)
                lista_jugadores.append(data_jugador)
                lista_ord = list_ganadores(lista_jugadores)
                data_jugador = []
                
                print ("\tTABLA DE POSICIONES")
                print ( "-" * 35)
                print ("  Jugador\t|\tN° Intentos")
                print ("=" * 35)

                for a in lista_ord:
                    print(f" {a[0]}\t|\t{a[1]}")
                    print ("=" * 35)

                seguir_jugando = input("""\n¿Desea seguir jugando?
                                            s -- Sí, quiero intentarlo de nuevo
                                            n -- No, ya me aburrí
                                            
                                            >>> ¿Qué desea? """)
                if seguir_jugando == "s" or seguir_jugando == "S":
                    data_jugador.append(nombre)
                    intentos = 0
              
                else:

                    perm_jugar = "n"
                    print ("\nQué bueno que lo hayas intentado. Esperamso que te hayas divertido")
                    input("\nPresione cualquier tecla para volver al menú... ")


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

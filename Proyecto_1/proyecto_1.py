#Este programa permite jugar TIC TAC TOE entre dos personas

import json

#*** FUNCIONES OPERATIVAS: MENÚ NOMBRES, PUNTAJES ***
#Función del menú principal
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 3:
                print ("Debe ser un numero de 1 a 6.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")


#***FUNCIONES DE ARCHIVO
#Función que me permite verificar si el archivo existe. SI no existe lo crea
def verificar_archivo (ruta):
    try:
        archivo = open(ruta, "r")
        lista_players = json.load(archivo)
        archivo.close
        return lista_players

    except:
        
        archivo = open(ruta, "w")
        json.dump([], archivo)
        archivo.close()
        archivo = open(ruta, "r")
        lista_players = json.load(archivo)
        archivo.close
        return lista_players
    
#Esta función registra el libro  
def registrar_player (dicc_player, ruta):
        list_id = []
        list_players_ord = []
        archivo = open(ruta, "r")
        lista_players = json.load(archivo)
        archivo.close()
        lista_players.append(dicc_player)
        for i in lista_players:
            id_i = list(i.keys())[0]
            list_id.append(int(id_i))
        list_id = sorted(list_id)

        for j in list_id:
            for k in lista_players:
                if str(j) == list(k.keys())[0]:
                    list_players_ord.append(k)

        archivo = open(ruta, "w")
        json.dump(list_players_ord, archivo)
        archivo.close()
        print ("\n", "-*" * 25)
        print ("| El libro se ha registrado correctamente |")
        print ( "-*" * 25)
        input ("\nPresione cualquier tecla para volver al menú principal... ")

#Esta función registra el libro  
def cargar_libro (lsta_libros, ruta):


        archivo = open(ruta, "w")
        json.dump(lsta_libros, archivo)
        archivo.close()


ruta = "Archivos/tic_winners.json" #ESTA CORRESPONDE A LA RUTA RELATIVA

while True:
    print ("\n\t  ","=" * 30)
    print (" \t  |        TIC - TAC - TOE       |")
    print ("\t  ","=" * 30)
    print ("\n\t       ", "-" * 20)
    opc = menu("""\t\t        MENÚ
                --------------------

                 1 -- Jugar.
                 2 -- Historial de mejores puntajes. 
                 3 -- SALIR.
                            >>>Elegir una opción [1 - 6]: """)
    
    if opc == 1:
        pass

    elif opc == 2:
        pass

    else:
        si_no = input("""\n¿Está seguro que desea salir? 
                      s -- Sí, deseo salir!!
                      n -- No, deseo continuar!!!""")
        if si_no == "s" or si_no == "S":
            print ("\nEL TABLERO ESTARÁ ESPERANDO POR UDS!!!")
            input ("\nPresione cualquier tecla para SALIR... ")
            break
        else:
            input ("\nPresione cualquier tecla para volver al menú... ")
            pass
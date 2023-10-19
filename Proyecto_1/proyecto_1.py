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


#Función que crea matrices de ceros
def crear_matrices_ceros (fil, col):
    m = []
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m

#Función que llena matrices consecutivos por fila
def llenar_matriz_1 (mat):
    n = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            n += 1 
            mat [f][c] = n 
    return mat

#***FUNCIONES DE ARCHIVO
#Función que me permite verificar si el archivo existe. SI no existe lo crea
def verificar_archivo (ruta):
    try:
        archivo = open(ruta, "r")
        lista_winners = json.load(archivo)
        archivo.close
        return lista_winners

    except:
        
        archivo = open(ruta, "w")
        json.dump([], archivo)
        archivo.close()
        archivo = open(ruta, "r")
        lista_winners = json.load(archivo)
        archivo.close
        return lista_winners
    
#Esta función registra el libro  
def registrar_player (dicc_winner, ruta):
        list_id = []
        list_winners_ord = []
        archivo = open(ruta, "r")
        lista_winners = json.load(archivo)
        archivo.close()
        lista_winners.append(dicc_winner)
        for i in lista_winners:
            id_i = list(i.keys())[0]
            list_id.append(int(id_i))
        list_id = sorted(list_id)

        for j in list_id:
            for k in lista_winners:
                if str(j) == list(k.keys())[0]:
                    list_winners_ord.append(k)

        archivo = open(ruta, "w")
        json.dump(list_winners_ord, archivo)
        archivo.close()
        print ("\n", "-*" * 25)
        print ("| El libro se ha registrado correctamente |")
        print ( "-*" * 25)
        input ("\nPresione cualquier tecla para volver al menú principal... ")

#Esta función registra el libro  
def cargar_libro (lsta_winners, ruta):


        archivo = open(ruta, "w")
        json.dump(lsta_winners, archivo)
        archivo.close()


ruta = "Proyecto_1/tic_prueba_1.json" #ESTA CORRESPONDE A LA RUTA RELATIVA
num_fil_col = 3

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
        verificar_archivo(ruta) #Verificación o creación del archivo
        dicc_winner = {}
        lista_winners = verificar_archivo(ruta)
        matriz_ceros = crear_matrices_ceros (num_fil_col, num_fil_col)
        matriz_llena = llenar_matriz_1 (matriz_ceros)
        #print (matriz_llena)
        print ("\n\t ", "*" * 37)
        print (" \t  *                                   *")
        print (" \t  *          VAMOS A JUGAR!!!         *")
        print (" \t  *                                   *")
        print ("\t ", "*" * 37)
        input ()

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
            
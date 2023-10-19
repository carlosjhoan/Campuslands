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

#menú para validar la ficha con la que desea jugar el player 1
def menu_fich(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 2:
                print ("Solo puedes marca 1 o 2.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")


#Validación del username
def valid_user(msj):
    while True:
        try:
            user = input(msj)

            return user

        except Exception as e:
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.", e)

def valid_fich(msj):
    while True:
        try:
            fich = input(msj)

            if fich.upper!='X' or fich.upper != 'O' :
                print (fich)
                print ("\n\t    ", "+" * 31)
                print ("\t     Solo puede ingresar 'X' u 'O'")
                print ("\t    ", "+" * 31)
                continue

            return fich

        except Exception as e:
            print ("\nERROR!!! Se ha producido un error. Inténtelo de nuevo.", e)

def valid_turno (lst, msj):
    while True:
        try:
            casilla = int(input(msj))
            if not casilla in lst:
                print ("\n\t    ", "+" * 40)
                print ("\t     Casilla ocupada. Intenta en otra.")
                print ("\t    ", "+" * 40)
                continue
            return casilla
        
        except ValueError:
            print ("\nSOLO SE PERMITE EL INGRESO DE NÚMEROS")


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

def mostrar_tablero (mat):
        print ("\n\t           -------------------")
        print ("\t           |     |     |     |")
        print (f"\t           |  {mat[0][0]}  |  {mat[0][1]}  |  {mat[0][2]}  |")
        print ("\t           |     |     |     |")
        print ("\t           -------------------")
        print ("\t           |     |     |     |")
        print (f"\t           |  {mat[1][0]}  |  {mat[1][1]}  |  {mat[1][2]}  |")
        print ("\t           |     |     |     |")
        print ("\t           -------------------")
        print ("\t           |     |     |     |")
        print (f"\t           |  {mat[2][0]}  |  {mat[2][1]}  |  {mat[2][2]}  |")
        print ("\t           |     |     |     |")
        print ("\t           -------------------")

#Va llenado la matriz con las marcas de los jugadores
def marcar_pos (mat, cas, fich):

    for i in range(len(mat)):
        for k in range(len(mat[0])):
            if cas == mat[i][k]:
                mat[i][k] = fich
    return mat

def autorizar_juego(lst):
    cont = 0
    for i in lst:
        if i == 0:
            cont += 1
    if cont == 9:
        return True
    
    else:
        return False

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
                            >>>Elegir una opción [1 - 3]: """)
    
    if opc == 1:
        verificar_archivo(ruta) #Verificación o creación del archivo
        dicc_winner = {}
        fich_x = "X"
        fich_o = "O"
        juego_on = "s"
        p1_on_off = "on"
        lista_casillas = list(range(1, 10))
        lista_winners = verificar_archivo(ruta)
        matriz_ceros = crear_matrices_ceros (num_fil_col, num_fil_col)
        matriz_llena = llenar_matriz_1 (matriz_ceros)
        #print (matriz_llena)
        print ("\n\t ", "*" * 37)
        print (" \t  *                                   *")
        print (" \t  *          VAMOS A JUGAR!!!         *")
        print (" \t  *                                   *")
        print ("\t ", "*" * 37)
        print ("\n\n\t          EL TABLERO ESTÁ LISTO...")
        print ("\n\t           -------------------")
        print ("\t           |     |     |     |")
        print ("\t           |     |     |     |")
        print ("\t           -------------------")
        print ("\t           |     |     |     |")
        print ("\t           |     |     |     |")
        print ("\t           -------------------")
        print ("\t           |     |     |     |")
        print ("\t           |     |     |     |")
        print ("\t           -------------------")
        player_1 = valid_user("\n\n\t   ¿Tu nombre de usuario, Player 1? ")
        print ("\n\t    ", "=-" * 20)
        print (f"\t     {player_1}, BIENVENIDO AL JUEGO.")
        print ("\t    ", "=-" * 20)
        player_2 = valid_user("\n\n\t   ¿Tu nombre de usuario, Player 2? ")
        print ("\n\t    ", "=-" * 20)
        print (f"\t     {player_2}, BIENVENIDO AL JUEGO.")
        print ("\t    ", "=-" * 20)
        fich_player_1 =menu_fich(f"""\n\t     ¿{player_1}, juegas con 'X' o con 'O'?
                                  \t     1 -- X
                                  \t     2 -- O
                                                >>> ¿Con cuál? [1-2] """)
        if fich_player_1 == 1:
            fich_player_1 = fich_x
            fich_player_2 = fich_o
            print ("\n\t    ", "-" * 25)
            print (f"\t     {player_1} jugará con {fich_player_1}")
            print (f"\t     {player_2} jugará con {fich_player_2}")
            print ("\t    ", "-" * 25)

        
        else:
            fich_player_2 = fich_x
            fich_player_1 = fich_o
            print ("\n\t    ", "-" * 25)
            print (f"\t     {player_1} jugará con {fich_player_1}")
            print (f"\t     {player_2} jugará con {fich_player_2}")
            print ("\t    ", "-" * 25)

        print ("\n\t   ", "+-" * 20)
        input (f"\t   {player_1}, presiona cualquier tecla para empezar el juego ")
        print ("\n\t ", "*" * 37)
        print (" \t  *                                   *")
        print (" \t  *             EMPIEZA!!!            *")
        print (" \t  *                                   *")
        print ("\t ", "*" * 37)


        while juego_on == "s":
            mostrar_tablero (matriz_llena)
            if p1_on_off == "on":
                print ("\n\t   ", "-*" * 15)
                mov_player_1 = valid_turno (lista_casillas, f"""\t   ¿{player_1}, en qué casilla marcas? \n\t   -*-*-*-*-*-*-*-*-*-*-*-*-*-*-* """)
                lista_casillas[mov_player_1-1] = 0
                matriz_llena = marcar_pos (matriz_llena, mov_player_1, fich_player_1)
                #mostrar_tablero (matriz_llena)
                if autorizar_juego(lista_casillas) == False:
                    p2_on_off = "on"
                    p1_on_off = "off"
                else:
                    p2_on_off = "off"
                    p1_on_off = "off"
                    juego_on = "n"

            
            else:
                print ("\n\t   ", "-*" * 10)
                mov_player_2 = valid_turno (lista_casillas, f"""\t   ¿{player_2}, en qué casilla marcas? \n\t-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* """)
                lista_casillas[mov_player_2-1] = 0
                matriz_llena = marcar_pos (matriz_llena, mov_player_2, fich_player_2)
                #mostrar_tablero (matriz_llena)
                if autorizar_juego(lista_casillas) == False:
                    p2_on_off = "off"
                    p1_on_off = "on"
                else:
                    p2_on_off = "off"
                    p1_on_off = "off"
                    juego_on = "n"


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
            
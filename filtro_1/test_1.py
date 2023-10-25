#Test_1
#Este programa lee archivos .csv con los registros de temperatura diarios de los diferentes observatorios del país
#Crea un archivo .json que contiene esta información
#Permite además observar los diferentes reportes.

#LIBRERÍAS UTILIZADAS
import json

#VALIDACIONES
#Función del menú principal
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 7:
                print ("Debe ser un numero de 1 a 6.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")



#Esta función valida el código y verifica que el código del observatorio exista
def verif_id (lst_registros, msj):
    while True:
        a = 0
        n = 0
        try:
            cod_obs  = input(msj)
            if not cod_obs.isdigit():
                print ("\n", "=." * 25)
                print ("El código de un observatorio se compone solo de números.\nVuélvalo a ingresar***")
                print ("=." * 25)
                continue

            for i in lst_registros:
                if list(i.keys())[0] == cod_obs:
                    n += 1
                    a = 1

                else:
                    pass
            if a == 0:
                print ("\n", "=." * 25)
                print ("El código no se encuentra registrado.\nIngrese uno existente***")
                print ("=." * 25)
                continue
            return cod_obs
        
        except Exception as e:
            print ("\n", "*-" * 25)
            print (f"\nHa ocurrido el siguiente error: {e}")
            print ("*-" * 25)


#Organiza en una lista las observaciones de un observatorio en particular. Para el punto 3
def reg_observatorio (lst_registros, cod_obs):
    lista_1_observatorio = []
    lista_1_years = []
    lsta_1_mes = []
    lsta_years = []
    for i in lst_registros:
        cod_i = list(i.keys())[0]
        if cod_i == cod_obs:
            lista_1_observatorio.append(i)
    
    
    #ordenar por año
    for j in lista_1_observatorio:
        cod_j = list(j.keys())[0]
        lsta_years.append((j[cod_j]["fecha"]["año"]))
           
    set_years = set(lsta_years)
    lsta_years = sorted(list(set_years))
   
    for j in lsta_years:
        for k in lista_1_observatorio:
            cod_k = list(k.keys())[0]
            if k[cod_k]["fecha"]["año"] == j:
                lista_1_years.append(k)
    
    #print (lista_1_years)
    
    #organizar por mes
    for p in range(len(lista_1_years)-1):
            year_p = lista_1_years[p][cod_obs]["fecha"]["año"]
            mes_p =  lista_1_years[p][cod_obs]["fecha"]["mes"]
            for q in range (p + 1, len(lista_1_years)):
                year_q = lista_1_years[q][cod_obs]["fecha"]["año"]
                mes_q =  lista_1_years[q][cod_obs]["fecha"]["mes"]

                if (year_p == year_q) and (int(mes_p) > int(mes_q)):
                    t = lista_1_years[p]
                    lista_1_years[p] = lista_1_years[q]
                    lista_1_years[q] = t


    #organizar por día
    for p in range(len(lista_1_years)-1):
            year_p = lista_1_years[p][cod_obs]["fecha"]["año"]
            dia_p = lista_1_years[p][cod_obs]["fecha"]["dia"]
            mes_p =  lista_1_years[p][cod_obs]["fecha"]["mes"]
            for q in range (p + 1, len(lista_1_years)):
                year_q = lista_1_years[q][cod_obs]["fecha"]["año"]
                dia_q = lista_1_years[q][cod_obs]["fecha"]["dia"]
                mes_q =  lista_1_years[q][cod_obs]["fecha"]["mes"]

                if (year_q == year_p) and (mes_p == mes_q) and (int(dia_p) > int(dia_q)):
                    t = lista_1_years[p]
                    lista_1_years[p] = lista_1_years[q]
                    lista_1_years[q] = t

    return lista_1_years

#Etsa funciónm permite ver la oinformación de un observatorio en particular
def inf_obs (lst_registros, cod_obs):

    lista_t_min = []
    lista_t_max = []
    lista_obs = []
    for i in lst_registros:
        cod_i = list(i.keys())[0]
        if cod_i == cod_obs:
            lista_obs.append(i)

    cant_obs = len(lista_obs)

    for j in lista_obs:
        lista_t_min.append(j[cod_obs]["temp_min"])
        lista_t_max.append(j[cod_obs]["temp_max"])
    
    max_temp = max(lista_t_max)
    min_temp = min(lista_t_min)
    prom_temp = (max_temp + min_temp)/2
    return max_temp, min_temp, prom_temp, cant_obs



#ARCHIVOS
#validación del nombre del archivo de registro


#FUNCIONES DE LISTAR 

#Esta función lista los observatorios por código
def listar_cod_1 (lst_registros):
    list_cod = []
    list_cod_nomb = []
    list_cod_1 = []
       
    for i in lst_registros:
        cod_i = list(i.keys())[0]
        list_cod.append(int(cod_i))
            
    set_cod = set(list_cod)
    list_cod = sorted(list(set_cod))
    
        
    for j in list_cod:
        list_cod_nomb.append(str(j))
        for k in lst_registros:
            cod_k = list(k.keys())[0]
            if str(j) == cod_k:
                nom_obs = k[str(j)]["nombre"]
        list_cod_nomb.append(nom_obs)
        list_cod_1.append(list_cod_nomb)
        list_cod_nomb = []
    
    return list_cod_1

#Esta función lista los observatorios por código
def listar_cod_2 (lst_registros):
    list_nomb = []
    list_nomb_cod = []
    list_cod_2 = []
       
    for i in lst_registros:
        cod_i = list(i.keys())[0]
        list_nomb.append(i[cod_i]["nombre"])
            
    set_nomb = set(list_nomb)
    list_nomb = sorted(list(set_nomb))
     
    for j in list_nomb:
        list_nomb_cod.append(j)
        for k in lst_registros:
            cod_k = list(k.keys())[0]
            if j == k[cod_k]["nombre"]:
                cod_list = cod_k
        list_nomb_cod.append(cod_list)
        list_cod_2.append(list_nomb_cod)
        list_nomb_cod = []
    
    return list_cod_2

##Esta función lista las observaciones a nivel por código y con paginación de 10
def listar_cod_5 (lst_registros):
    list_cod = []
    
    list_cod_5 = []
       
    for i in lst_registros:
        cod_i = list(i.keys())[0]
        list_cod.append(int(cod_i))
            
    set_cod = set(list_cod)
    list_cod = sorted(list(set_cod))
    
        
    for j in list_cod:
        
        for k in lst_registros:
            cod_k = list(k.keys())[0]
            if str(j) == cod_k:
                list_cod_5.append(k)
        
    return list_cod_5

#Función que me permite verificar si el archivo .json existe. SI no existe lo crea
def verificar_archivo (ruta):
    try:
        archivo = open(ruta, "r")
        lista_libros = json.load(archivo)
        archivo.close
        return lista_libros

    except:
        
        archivo = open(ruta, "w")
        json.dump([], archivo)
        archivo.close()
        archivo = open(ruta, "r")
        lista_libros = json.load(archivo)
        archivo.close
        return lista_libros


#validación del archivo .csv con los registros:
#INFORMACIÓN IMPORTANTE:La fecha en el archivo .csv está en formato "dd-mm-aaa"
def verificar_registro_csv (ruta_csv):
    try:
        lista_sin_format = []
        lista_con_format = []
        dicc_reg = {}
        observacion = open(ruta_csv, "r")
        for i in observacion:
            lista_sin_format.append(i.split(";"))
        
        

        for j in lista_sin_format[1:]:
            cod = j[0].strip()
            nombre_obs = j[1].strip()
            t_max = float(j[2].strip())
            t_min = float(j[3].strip())
            fecha = j[4].strip()
            fecha = fecha.split("/")
            dia = fecha[0]
            mes = fecha[1]
            year = fecha[2]


            dicc_reg[cod] = {"nombre": nombre_obs,"fecha": {"dia": dia, "mes" : mes, "año": year},"temp_max" : t_max,"temp_min" : t_min}
            lista_con_format.append(dicc_reg)
            dicc_reg = {}

          
        observacion.close
        return lista_con_format

    except Exception as e:
        print (f"\nEl archivo no corresponde al registro de los observatorios.")
        input ("Presione cualquier tecla para salir")
        

#Función que me permite verificar si el archivo .json existe. SI no existe lo crea
def verificar_archivo_json (ruta_json):
    try:
        archivo = open(ruta_json, "r")
        lista_registros_obs = json.load(archivo)
        archivo.close
        return lista_registros_obs

    except:
        
        archivo = open(ruta_json, "w")
        json.dump([], archivo)
        archivo.close()
        archivo = open(ruta_json, "r")
        lista_registros_obs = json.load(archivo)
        archivo.close
        return lista_registros_obs

#Esta función registra la información actualizada al json 
def cargar_libro (lsta_registros, ruta_json):


        archivo = open(ruta_json, "w")
        json.dump(lsta_registros, archivo)
        archivo.close()
    
#Esta función me permite añadir los datos del registro csv al json. Me devulve la lista de información completa.
def csv_json (lst_csv, lst_json):
    for i in lst_csv:
        lst_json.append(i)

    return lst_json
   


#DESARROLLO DEL PROGRAMA
 #archivo .csv con los registros diarios de temperatura. Su nombre es la fecha del registro [dia-mes-año]
archivo_json = "obervatorios.json" #Este es el nombre del archivo .json que contiene la información de todos los observatorios. Recogida diariamente
carpeta = "filtro_1"

#RUTAS: json y csv
ruta_csv = "filtro_1/datos.csv" #Ruta del registro diaro de datos (formato csv)
ruta_json = f"{carpeta}/{archivo_json}" #Ruta del archivo que contiene el historial de los registros(formato json)

#LEER LISTAS y CARGARLAS AL JSON
lista_csv = verificar_registro_csv (ruta_csv)
lista_json = verificar_archivo_json (ruta_json) #Inicializar archivo json
lista_registro_obs = lista_csv #Lista con la información actualizada
cargar_libro (lista_csv, ruta_json)
while True:
    
    
    

    opc = menu("""MENÚ
               1. Listado de observatorios (por código)
               2. Listado de observatorios (por nombre)
               3. Listado de observaciones de un observatorio
               4. Información de un observatorio
               5. Listado de observaciones a nivel nacional (por código)
               6. Listado de observaciones a nivel nacional (por promedio de temperatura)
               7. SALIR

               >> Indicar opción [1 - 7]: """)
    
    if opc == 1:
        #print (listar_cod_1 (lista_registro_obs))
        print ("\n      1. LISTADO DE OBSERVACIONES POR CÓDIGO")
        print ("\t", "-" * 40)
        print ("\n\n", "=" * 24)
        print("|CÓDIGO\t|   NOMBRE\t|")
        print ( "=" * 25)

        for i in listar_cod_1 (lista_registro_obs):
            if len(i[1]) <= 5:
                i[1] = i[1] + " "
            print (f"| {i[0]}\t| {i[1]}\t|")
            print ("." * 25)

        input("Presiona cualquier tecla para volver al menú... ")
                  
                  

    elif opc == 2:
        #print (listar_cod_2 (lista_registro_obs))
        print ("\n      2. LISTADO DE OBSERVACIONES POR NOMBRE")
        print ("\t", "-" * 40)
        print ("\n\n", "=" * 24)
        print("| NOMBRE\t|CODIGO |")
        print ( "=" * 25)

        for i in listar_cod_2 (lista_registro_obs):
            if len(i[0]) <= 5:
                i[0] = i[0] + " "
            print (f"| {i[0]}\t| {i[1]}\t|")
            print ("." * 25)

        input("Presiona cualquier tecla para volver al menú... ")

    elif opc == 3:
        print ("\n      3. LISTADO DE OBSERVACIONES DE UN OBSERVATORIO")
        print ("     ", "-" * 47)
        print ("\n\n", "=" * 72)

        print("|CÓDIGO\t|   NOMBRE\t|")
        print ( "=" * 25)

        for i in listar_cod_1 (lista_registro_obs):
            if len(i[1]) <= 5:
                i[1] = i[1] + " "
            print (f"| {i[0]}\t| {i[1]}\t|")
            print ("." * 25)

        cod_obs = verif_id (lista_registro_obs,"\nIngrese el código del observatorio que desea consultar:\n>>> ")
        lista_ordenada = reg_observatorio (lista_registro_obs, cod_obs)

        for i in lista_registro_obs:
            cod_i = list(i.keys())[0]
            nombre = i[cod_i]["nombre"]
        
        print ("\n\n", ":" * 30)
        print (f"OBSERVATORIO: {nombre}")
        print ( ":" * 30, )
        for j in lista_ordenada:
            cod_j = list(j.keys())[0]
            dia = j[cod_j]["fecha"]["dia"]
            mes = j[cod_j]["fecha"]["mes"]
            year = j[cod_j]["fecha"]["año"]
            temp_max = j[cod_j]["temp_max"]
            temp_min = j[cod_j]["temp_min"]
            print(f"\nFecha de registro: {dia} / {mes} / {year}")
            print (f"Temperatura máxima: {temp_max} [°C]")
            print (f"Temperatura máxima: {temp_min} [°C]")
            print ("." * 30)

        input("\nPresiona cualquier tecla para volver al menú... ")





        

    elif opc == 4:
        print ("\n      4. INFORMACIÓN DE UN OBSERVATORIO")
        print ("\t", "-" * 40)
        print ("\n\n", "=" * 24)
        

        print("|CÓDIGO\t|   NOMBRE\t|")
        print ( "=" * 25)

        for i in listar_cod_1 (lista_registro_obs):
            if len(i[1]) <= 5:
                i[1] = i[1] + " "
            print (f"| {i[0]}\t| {i[1]}\t|")
            print ("." * 25)

        cod_obs = verif_id (lista_registro_obs,"\nIngrese el código del observatorio que desea consultar:\n>>> ")
        lista_info_obs = inf_obs (lista_registro_obs, cod_obs)
        for i in lista_registro_obs:
            cod_i = list(i.keys())[0]
            nombre = i[cod_i]["nombre"]
        
        print ("\n\n", ":" * 35)
        print (f"OBSERVATORIO: {nombre}")
        print ( ":" * 35, )
        print (f"   Cantidad de observaciones: {lista_info_obs[3]}")
        print (f"   Temperatura máxima: {lista_info_obs[0]} [°C]")
        print (f"   Temperatura mínima: {lista_info_obs[1]} [°C]")
        print (f"   Temperatura promedio: {lista_info_obs[2]:.2f} [°C]")
        print ("_" * 35)

        


    elif opc == 5:
        #print (listar_cod_2 (lista_registro_obs))
        n = 0
        print ("\n      5. LISTADO DE OBSERVACIONES NACIONALES")
        print ("\t", "-" * 40)
        print ("\n\n", "=" * 72)

        
        
        for i in listar_cod_5 (lista_registro_obs):
            cod_i = list(i.keys())[0]
            nombre = i[cod_i]["nombre"]
            if len(nombre) <= 5:
                nombre = nombre + "  "
            t_max = i[cod_i]["temp_max"]
            t_min = i[cod_i]["temp_min"]
            t_prom = (t_max + t_min)/2
            print (f"| {cod_i}\t| {nombre}\t|  \t{t_max}\t|  \t{t_min}\t|  \t{t_prom:.2f}\t|")
            print ("." * 73)
            n += 1
            if n == 10:
                n = 0
                input (">>> Seguir [ENTER] --> \n")

        input("\nPresiona cualquier tecla para volver al menú... ")


    elif opc == 6:
        pass

    else: 
        si_no = input("""\n¿Está seguro que desea salir? 
                      s -- Sí, deseo salir!!
                      n -- No, deseo continuar!!!
                      
                      >>> ¿Opción [s/n]?: """)
        
        if si_no == "s" or si_no == "S":
            print ("\nEsperamos haberle sido de utilidad.")
            input ("\nPresione cualquier tecla para SALIR... ")
            break
        else:
            input ("\nPresione cualquier tecla para volver al menú... ")
            
    

            